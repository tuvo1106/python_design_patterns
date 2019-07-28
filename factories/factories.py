"""
Factories
 - A component responsible solely for the wholesale (not piecewise)
   creation of objects

Motivation
 - Object creation logic becomes too convoluted
 - Initializer is not descriptive
   - Name is always __init__
   - Cannot overload with same sets of arguments with
     different names
   - Can turn into 'optional parameter hell'
 - Wholesale object creation (non-piecewise, unlike Builder)
   can be outsourced to
   - A separate method (Factory Method)
   - That may exist in a separate clas (Factory)
   - Can create a hiearchy of factories of Abstract Factory
"""

from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # naive
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system === CoordinateSystem.CARTESIAN:
    #         self.a = a
    #         self.b = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


p = Point(2, 3)
print(p)
p2 = Point.new_polar_point(1, 2)
print(p2)
