from PyVec import PyVec

# The simplest way of creating a new vector is by just specifying its values
# There are no limitations in size

# This Vector has 3 entries
vec3 = PyVec(1, 2, 3)
print(vec3.get_vec())  # calling get_vec() on any PyVec object will return its Vector as tuple.

# This one has 2...
vec2 = PyVec(11, 22)

# And this one 5
vec5 = PyVec(10, 20, 30, 40, 50)


# You can also create Vectors by giving them a default size and have them filled with a default value
# by default the default value will be zero
vecA = PyVec(size=3)

# You can change the default value, if you want to...
vecB = PyVec(size=3, default=2)


# of course you can combine these two methods
vecC = PyVec(1, 2, size=4)


# PyVec also has macros by which you can reference certain positions of a Vector
# by default these macros are x, y, z
print(vec3.x)
print(vec3.y)
print(vec3.z)

# if the amount of macros is greater than the size of a vector the redundant macros will be removed so if the vector
# is 2 long, than calling the first two default macros on that Vector will still work, even tho there were originally 3 macros
print(vec2.x)
print(vec2.y)

# You can also set your own macros
vecRGBA = PyVec(size=4, default=255, macros=("r", "g", "b", "a"))
vecRGBA.g = 0
vecRGBA.b = 0
print(vecRGBA.get_vec())
