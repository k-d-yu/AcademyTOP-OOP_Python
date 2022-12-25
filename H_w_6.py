import math


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            if length is None:
                self._width = self._length = width
            else:
                self._width = width
                self._length = length
        else:
            self._radius = radius

    def area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод нахождения площади(area())")


class Rectangle(Table):
    def area(self):
        print(self._width * self._length)


class Round(Table):
    def area(self):
        print(round(math.pi * self._radius ** 2, 2))


rect1 = Rectangle(20, 10)
print(rect1.__dict__)
rect1.area()
rect2 = Rectangle(20)
print(rect2.__dict__)
rect2.area()
r = Round(radius=20)
print(r.__dict__)
r.area()
