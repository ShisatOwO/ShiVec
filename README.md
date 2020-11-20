# ShiVec
> __ShiVec is a simple, pure python module for working with vectors.__

I always kind of skipped writing a vector implementation for my programs or just hacked a quick solution together, which is (obviously) not optimal, so I decided to 
write a proper one I could use in all of my projects. My goal was to make it flexible and easy to use. Since ShiVec is the first project of mine that I want to 
publish, it is also a way for me to learn about developing and publishing software, so feedback is highly appreciated :)

### Installation (python 3.8 and up)
```python
pip install ShiVec
```

### Quick example
```python
from ShiVec import ShiVec

# Declaring a new vector "vecA"
vecA = ShiVec(1, 2, 3)

# Declaring a new vector "vecB" by specifying it's size
vecB = ShiVec(size=3)
```
