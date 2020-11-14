"""
ShiVec: Written by Shisato (https://github.com/ShisatOwO/) and Licensed under the MIT License
"""


import math


def is_shivec(other):
    if not isinstance(other, ShiVec):
        raise Exception("[ShiVec] " + str(other) + " is not a ShiVec object")
    return True


class ShiVec:
    def __init__(self, *args, macros=("x", "y", "z"), **kwargs):
        """Create a new Vector. Either the size parameter or values are required, the other parameters are optional.
        For example: A vector containing 3 entries can be defined like this ShiVec(1, 2, 3) or like this ShiVec(size=3)"""

        self._vec = []
        self._deflt = 0
        self._macros = macros

        # setting the default value and size of the vector
        if "size" in kwargs:
            self._size = kwargs["size"]
            if "default" in kwargs:
                self._deflt = kwargs["default"]
            if len(args) > self._size:
                raise Exception("[ShiVec] Values gives were bigger than the specified size of the vector")
        else:
            if len(args) != 0:
                self._size = len(args)
            else:
                raise Exception("[ShiVec] Vector size was not specified and XYZ Values were not given. \n\tSOLUTION: Either "
                                "specify a size, so the Vector can be initialized with default values or provide "
                                "actual values to fill the Vector")

        # Are the macros valid ?
        if not isinstance(self._macros, tuple) and not isinstance(self._macros, list):
            raise Exception("[ShiVec] Macros must be strings contained in a tuple or list.They also must not start with a number/punctuation mark or be empty. "
                            "For example ShiVec(size=3, macros=(\"r\", \"g\", \"b\") is a valid call")
        for m in self._macros:
            if not isinstance(m, str) or m == "":
                raise Exception("[ShiVec] Macros must be strings contained in a tuple or list.They also must not start with a number/punctuation mark or be empty."
                                " For example ShiVec(size=3, macros=(\"r\", \"g\", \"b\") is a valid call")
            if not m[0].isalpha():
                raise Exception(
                    "[ShiVec] Macros must be strings contained in a tuple or list.They also must not start with a number/punctuation mark or be empty."
                    " For example ShiVec(size=3, macros=(\"r\", \"g\", \"b\") is a valid call")

        # Is the default value valid ?
        if not isinstance(self._deflt, int) and not isinstance(self._deflt, float):
            raise Exception("[ShiVec] Default value must be int or float")

        # TODO: Should *args be checked if it only contains int or float ?

        # Checking if there are more macros than the vector has entries? If yes, remove the unnecessary macros
        if len(macros) > self._size:
            self._macros = macros[:self._size]

        # Filling _vec with default values
        for i in range(self._size):
            self._vec.append(self._deflt)

        # Filling _vec with values from *args
        for i in range(len(args)):
            self._vec[i] = args[i]

        # Create macros
        self._apply_vec_to_macros()

    def _apply_macros_to_vec(self):
        """Overwrites specific entries of _vec with its corresponding macro, this should be done everytime before something is done with _vec."""
        for i in range(len(self._macros)):
            if (x := getattr(self, self._macros[i], None)) is None:
                raise Exception("Something went really wrong while trying to apply macros to the Vector")
            self._vec[i] = x

    def _apply_vec_to_macros(self):
        """Overwrites all macros with their corresponding entry in _vec, this should be done everytime something was done with _vec."""
        for i in range(len(self._macros)):
            setattr(self, self._macros[i], self._vec[i])

    def _check_size(self, other):
        """Checks whether the given parameter is a ShiVec object or not, and if its size matches with _size."""
        is_shivec(other)
        if self._size != other._size:
            raise Exception("[ShiVec] The Size of the Vectors does not match")

    def _operation(self, other, code):
        """Makes working with other vector easier, checks if the other vectors size is ok and applies macros and updates macros, it executes code passed as function taking the other vector as parameter
        between applying the macros and updating them."""
        self._check_size(other)
        self._apply_macros_to_vec()
        out = code(other)
        self._apply_vec_to_macros()
        return out

    def _operation_nov(self, code, *args, **kwargs):
        """Applies macros to the vector than executes, the method passed trough the code argument and finally updates the macros"""
        self._apply_macros_to_vec()
        out = code(*args, **kwargs)
        self._apply_vec_to_macros()
        return out

    def get_vec(self, iindex=None):
        """Returns Vector as a tuple, or a specified index"""
        i = iindex
        self._apply_macros_to_vec()
        if iindex is None:
            return tuple(self._vec)
        if iindex in self._macros:
            i = self._macros.index(iindex)
        return self._vec[i]

    def set_vec(self, iindex, val):
        """Sets index iindex of the vector to val"""
        i = iindex
        if iindex in self._macros:
            i = self._macros.index(iindex)
        self._vec[i] = val
        self._apply_vec_to_macros()

    def add(self, other):
        """Adds this vector and another ShiVec vector, vectors must have the same size"""
        def code(v):
            for i in range(self._size):
                self._vec[i] += v._vec[i]
        self._operation(other, code)

    def sub(self, other):
        """Subtracts another ShiVec vector from this Vector, vectors must have the same size"""
        def code(v):
            for i in range(self._size):
                self._vec[i] -= v._vec[i]
        self._operation(other, code)

    def mul(self, other):
        """Calculates the scalar product of this vector and another ShiVec vector, vectors must have the same size"""
        def code(v):
            for i in range(self._size):
                self._vec[i] *= v._vec[i]
        self._operation(other, code)

    def scalar(self, other):
        """Multiplies this vector with a scalar"""
        self.mul(ShiVec(size=self._size, default=other))

    def dot(self, other):
        """Calculates dot product"""
        def code(v):
            s = 0
            for i in range(self._size):
                s += self._vec[i] * v._vec[i]
            return s
        return self._operation(other, code)

    def div(self, other):
        """Divides this vector by another ShiVec vector"""
        def code(v):
            for i in range(self._size):
                self._vec[i] /= v._vec[i]
        self._operation(other, code)

    def norm(self):
        """Normalizes this vector"""
        def code(*args, **kwargs):
            l = self.length()
            for i in range(self._size):
                self._vec[i] /= l
        self._operation_nov(code)

    def length(self):
        """Calculates the vectors length"""
        def code(*args, **kwargs):
            s = 0
            for i in self._vec:
                s += i*i
            return math.sqrt(s)
        return self._operation_nov(code)

    def duplicate(self):
        """Duplicates this Vector"""
        def code(*args, **kwargs):
            v = ShiVec(size=self._size, macros=self._macros, default=self._deflt)
            v._vec = self._vec
            v._apply_vec_to_macros()
            return v
        return self._operation_nov(code)

    def __str__(self):
        return str(self.get_vec())

    def __iter__(self):
        return iter(self.get_vec())

    def __add__(self, other):
        v = self.duplicate()
        v.add(other)
        return v

    def __sub__(self, other):
        v = self.duplicate()
        v.sub(other)
        return v

    def __mul__(self, other):
        v = self.duplicate()
        if isinstance(other, ShiVec):
            v.mul(other)
        else:
            v.scalar(other)
        return v
