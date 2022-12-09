import math


class Rectangle:
    def __init__(self, length, width):
        self.__length = self.__width = 0
        if Rectangle.__check_value(length) and Rectangle.__check_value(width):
            self.__length = length
            self.__width = width

    def __check_value(value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    def set_length(self, length):
        if Rectangle.__check_value(length):
            self.__length = length
        else:
            print("Длина прямоугольника должна быть числом!")

    def get_length(self):
        return f"Длина прямоугольника: {self.__length}"

    def set_width(self, width):
        if Rectangle.__check_value(width):
            self.__width = width
        else:
            print("Ширина прямоугольника должна быть числом!")

    def get_width(self):
        return f"Ширина прямоугольника: {self.__width}"

    def area(self):
        return f"Площадь прямоугольника: {self.__length * self.__width}"

    def perimetr(self):
        return f"Периметр прямоугольника: {(self.__length + self.__width) * 2}"

    def hypotenuse(self):
        return f"Гипотенуза прямоугольника: {round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)}"

    def draw(self):
        for i in range(self.__length):
            for j in range(self.__width):
                print("*", end=" ")
            print()
        return ""


r1 = Rectangle(3, 9)
print(r1.get_length())
print(r1.get_width())
print(r1.area())
print(r1.perimetr())
print(r1.hypotenuse())
print(r1.draw())

r1.set_length(2)
r1.set_width(4)
print(r1.get_length())
print(r1.get_width())
print(r1.area())
print(r1.perimetr())
print(r1.hypotenuse())
print(r1.draw())


