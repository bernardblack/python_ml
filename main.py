from __future__ import annotations
from abc import abstractmethod
from typing import final
import math
import random
import re


class Shape:
    """ One of my favourite places to visit is the two-dimensional world
    described in Edwin Abbott’s mathematical fantasy, Flatland. """

    all_shapes = []
    pi = 3.14159

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.__class__.all_shapes.append(self)

    @abstractmethod
    def get_vertex(self):
        raise NotImplementedError("Method get_vertex not defined in Shape")

    @abstractmethod
    def get_area(self):
        raise NotImplementedError("Method get_area not defined in Shape")

    @classmethod
    def get_all_shapes(cls):
        return cls.all_shapes
    
    @final
    def get_center(self):
        return self.x, self.y

    @final
    def move(self, x, y):
        self.x = x
        self.y = y

    @final
    def swap(self, shape: Shape):
        x, y = shape.get_center()
        shape.move(self.x, self.y)
        self.move(x, y)

    @final
    def get_distance(self, shape: Shape):
        x, y = shape.get_center()
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    @staticmethod
    def say_hi():
        return "from Shape class"


class NameOfShape:

    def __init__(self, name="unstable"):
        self.name = name

    def get_name(self):
        return self.name

    @staticmethod
    def say_hi():
        return "from NameOfShape class"


class Circle(Shape, NameOfShape):

    def __init__(self, x=0, y=0, radius=1, name="testing"):
        Shape.__init__(self, x, y)
        NameOfShape.__init__(self, name)
        self.radius = radius

    def get_area(self):
        return self.pi * self.radius ** 2

    def get_vertex(self):
        return self.x, self.y + self.radius


class Triangle(NameOfShape, Shape):

    def __init__(self, x=0, y=0, side=1, name="testing"):
        Shape.__init__(self, x, y)
        NameOfShape.__init__(self, name)
        self.side = side

    def get_vertex(self):
        return math.sqrt(3) / 2 * self.x / 2, self.y

    def get_area(self):
        return self.side ** 2 * math.sqrt(3) / 4


class Square(Shape, NameOfShape):

    def __init__(self, x=0, y=0, side=1, name="testing"):
        Shape.__init__(self, x, y)
        NameOfShape.__init__(self, name)
        self.side = side

    def get_vertex(self):
        return self.x, self.y / 2

    def get_area(self):
        return self.side ** 2


def main():

    flatland = [Triangle(3, 3, 3, "Buzz"), Circle(-3, -3, 3, "Rex"), Square(3, -5, 4, "Bo"),
                Triangle(-5, -5, 3, "Hamm"), Square(1, 1, 1, "Slink"), Circle(1, 101001101, 5, "Potato"), 
                Triangle(-5, -5, 3, "Woody"), Square(10, -10, 7, "Sarge"), Triangle(-100, -200, 150, "Etch"), Circle(20, -20, 10, "Lenny")]

    def show_shapes():
        for shape in Shape.all_shapes:
            shape_type = re.search(r"__main__.(.*)'>", str(shape.__class__)).group(1)
            print(f"{shape.get_name()} is {shape_type}")
            print(f"coordinates: {shape.get_center()}, vertex: {shape.get_vertex()}, area: {shape.get_area()}, say_hi() {shape.say_hi()}")

    def show_distance():
        for i in range(0, len(flatland)):
            for j in range(i + 1, len(flatland)):
                if i != j:
                    shape = flatland[i]
                    shape2 = flatland[j]
                    print(f"Distance between {shape.get_name()} {shape.get_center()} and {shape2.get_name()} {shape2.get_center()} is {shape.get_distance(shape2)}")

    def shuffle():
        print("\n*** Shuffle ***\n")
        for i in range(0, 100):
            j = random.randrange(0, len(flatland), 1)
            k = random.randrange(0, len(flatland), 1)
            if j != k:
                flatland[j].swap(flatland[k])

    def quake():
        print("\n*** Quake ***\n")
        for shape in Shape.all_shapes:
            x, y = shape.get_center()
            x_offset = random.randrange(-500, 500, 1)
            y_offset = random.randrange(-500, 500, 1)
            shape.move(x + x_offset, y + y_offset)

    for i in range(0, 6):
        show_shapes()
        show_distance()
        shuffle()
        quake()


if __name__ == "__main__":
    main()
