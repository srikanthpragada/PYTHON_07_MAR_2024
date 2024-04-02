from abc import abstractmethod, ABC
import math


class Shape(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [Circle(10, 20, 15),
          Square(10, 10, 20),
          Circle(10, 30, 10)]

for s in shapes:
    print(s.area())
