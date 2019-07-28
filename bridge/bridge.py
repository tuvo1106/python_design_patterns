"""
Bridge
- A mechanism that decouples an interface (hierarchy) from an implementation
  (hierarchy)
Motivation
- Prevents a 'Cartesian product' complexity explosion
"""

from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    # render square


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # bridge
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

RASTER = RasterRenderer()
VECTOR = VectorRenderer()
CIRCLE = Circle(VECTOR, 5)
CIRCLE.draw()
CIRCLE.resize(2)
CIRCLE.draw()
CIRCLE = Circle(RASTER, 5)
CIRCLE.draw()
CIRCLE.resize(2)
CIRCLE.draw()
