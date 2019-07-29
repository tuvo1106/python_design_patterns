from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('Cannot apply same decorator twice')
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100}% transparency'

if __name__ == "__main__":
    CIRCLE = Circle(2)
    print(CIRCLE)

    RED_CIRCLE = ColoredShape(CIRCLE, 'red')
    print(RED_CIRCLE)

    RED_HALF_TRANS_CIRCLE = TransparentShape(RED_CIRCLE, 0.5)
    print(RED_HALF_TRANS_CIRCLE)

    MIXED = ColoredShape(ColoredShape(CIRCLE, 'red'), 'green')
    print(MIXED)
