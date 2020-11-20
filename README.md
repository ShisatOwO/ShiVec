# ShiVec
__ShiVec is a simple, pure python module for working with vectors.__

I always kind of skipped writing a vector implementation for my programs or just hacked a quick solution together, which is (obviously) not optimal, so I decided to 
write a proper one I could use in all of my projects. My goal was to make it flexible and easy to use. Since ShiVec is the first project of mine that I want to 
publish, it is also a way for me to learn about developing and publishing software, so feedback is highly appreciated :)

### Installation (Python 3)
```python
pip install ShiVec
```

### Quick example
> NOTE: For a more detailed example and explanation, please take a look at ShiVecs wiki or example.py  

```python
from ShiVec import ShiVec

# Declaring a new vector "vecA"
vecA = ShiVec(1, 2, 3)
print("vecA: ", vecA)


# Declaring a new vector "vecB" by specifying it's size.
# This will initialize a vector containing 3 zeros
vecB = ShiVec(size=3)
print("vecB: ", vecB)


# By default a vectors default value will be 0. To use a different value do the following:
vecC = ShiVec(size=3, default=2)
print("vecC: ", vecC)


# ShiVecs vectors have macros, (x, y, z) by default
vecA.x = 100
# print(vecA.x)
# print(vecA.y)
# print(vecA.z)
print("vecA: \tx: {} \t y: {} \t z: {}".format(vecA.x, vecA.y, vecA.z))


# Of course you can combine all of those declaration methods and set custom macros
rgba = ShiVec(165, 234, size=4, default=255, macros=("r", "g", "b", "a"))
# print(rgba.r)
# print(rgba.g)
# print(rgba.b)
# print(rgba.a)
print("rgba: ", rgba)


# Calling get_vec() on a ShiVec object retuns the current vector as tuple
vecA_as_tuple = vecA.get_vec()

# Use indexes or macros to get a certain value
vecAX = vecA.get_vec(0)
vecAY = vecA.get_vec("y")


# Example of addition:
print("vecA + vecC =", vecA + vecC)  # This method does not change any of the vectors involved, it just returns the sum

# Alternative way:
vecA.add(vecC)  # This method however, adds vecC to vecA and overwrites vecAs contents with the sum
print("vecA + vecC =", vecA)
```
