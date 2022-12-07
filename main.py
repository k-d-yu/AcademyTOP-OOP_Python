# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# # print(Point.__doc__)
# # print(dir(Point))
#
# p1 = Point()
# p2 = Point()
# print("p1 = ", p1.x)
# print("p2 = ", p2.x)
# print("Point = ", Point.x)
# # print(type(p1))
# p1.x = 100
# p2.x = 200
# print("p1 = ", p1.x)
# print("p2 = ", p2.x)
# print("Point = ", Point.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y = 300
# print("p1 = ", p1.y)
# print("p2 = ", p2.y)
# print("Point = ", Point.y)

# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(Point.__dict__)


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# print(p1.x)
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)
# p2 = Point()
# p2.x = 2
# p2.y = 7
# p2.set_coord()

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# print(p1.x)
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2, 5, 8)
# print(p2.__dict__)

class Human:
    name = "name"
    birthday = "00.00.0000"
    phone = "00-00-00"
    country = "country"
    city = "city"
    address = "street"

    def print_info(self):
        print(" Персональные данные ".center(40, "*"))
        print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
              f"Страна: {self.country}\nГород: {self.city}\nАдрес: {self.address}")
        print("=" * 40)

    def input_info(self, first_name, birthday, phone, country, city, address):
        self.name = first_name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):  # установить имя
        if isinstance(name, str):
            self.name = name

    def get_name(self):  # получить имя
        return self.name

    def set_birthday(self, bth):
        self.birthday = bth

    def get_birthday(self):
        return self.birthday


h1 = Human()
h1.print_info()
h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
h1.print_info()
h1.set_name("Алевтина")
h1.print_info()
print(h1.get_name())
h1.set_birthday("23.01.1987")
print(h1.get_birthday())
