import math

class Vector:
    def __init__(self, x=0, y=0):
        print("__init__ self:",self,"x:", x, "y:",y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        print("__repr__ self:",self)
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __add__(self, other):
        print("__add__ self:",self,"other:",other)
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

v1 = Vector(2, 4)
v2 = Vector(2, 1)

v3 = v1 + v2
print(v3)