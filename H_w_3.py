import math


class Area:
    __count = 0

    @staticmethod
    def triangle_ger(a, b, c):
        Area.__count += 1
        p = (a + b + c) // 2
        return f"Площадь треугольника по формуле Герона ({a},{b},{c}): {math.sqrt(p * (p - a) * (p - b) * (p - c))}"

    @staticmethod
    def triangle_osn(a, h):
        Area.__count += 1
        return f"Площадь треугольника через основание и высоту ({a},{h}): {0.5 * a * h}"

    @staticmethod
    def square(a):
        Area.__count += 1
        return f"Площадь квадрата ({a}): {a ** 2}"

    @staticmethod
    def rectangle(a, b):
        Area.__count += 1
        return f"Площадь прямоугольника ({a},{b}): {a * b}"

    @staticmethod
    def get_count():
        return f"Количество подсчетов площади: {Area.__count}"


print(Area.triangle_ger(3, 4, 5))
print(Area.triangle_osn(6, 7))
print(Area.square(7))
print(Area.rectangle(2, 6))
print(Area.get_count())
