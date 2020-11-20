# ShiVec
__ShiVec is a simple, pure python module for working with vectors.__

I always kind of skipped writing a vector implementation for my programs or just hacked a quick solution together, which is (obviously) not optimal, so I decided to 
write a proper one I could use in all of my projects. My goal was to make it flexible and easy to use. Since ShiVec is the first project of mine that I want to 
publish, it is also a way for me to learn about developing and publishing software, so feedback is highly appreciated :)

### Installation (Python 3.8 and up)
```python
pip install ShiVec
```

### Quick example
> NOTE: For a more detailed example and explanation, please take a look at ShiVecs wiki or example.py  

```python
from ShiVec import ShiVec

# Declaring a new vector "vecA"
vecA = ShiVec(1, 2, 3)
print(vecA)


# Declaring a new vector "vecB" by specifying it's size.
# This will initialize a vector containing 3 zeros
vecB = ShiVec(size=3)
print(vecB)


# By default a vectors default value will be 0. To use a different value do the following:
vecC = ShiVec(size=3, default=2)
print(vecC)


# ShiVecs vectors have macros, (x, y, z) by default
vecA.x = 100
print("vecA: \tx {vecA.x} \t y: {vecA.y} \t z: {vecA.z}")


# Of course you can combine all of those declaration methods and set custom macros
rgba = ShiVec(165, 234, size=4, default=255, macros=(r, g, b, a))


# Calling get_vec()... to be continued...
```
