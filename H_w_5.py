class Auto:
    def __init__(self, name, year, maker, power, color, price):
        self.name = name
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

    @staticmethod
    def verify_year(year):
        if not isinstance(year, (int, float)):
            raise TypeError("Год должен быть числом.")
        if year > 2022:
            raise TypeError("Не соответствующий год.")

    @staticmethod
    def verify_price(price):
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом.")

    @staticmethod
    def verify_maker(maker):
        m = maker.upper()
        if m != maker:
            raise TypeError("Производителя необходимо вводить заглавными!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.verify_year(year)
        self.__year = year

    @property
    def maker(self):
        return self.__maker

    @maker.setter
    def maker(self, maker):
        self.verify_maker(maker)
        self.__maker = maker

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.verify_price(price)
        self.__price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.maker}\nМощность "
              f"двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 30)


a1 = Auto("X7 M50i", 2021, "BMW", "530 л.с.", "white", 10790000)
a1.print_info()
a1.name = "CX-5"
a1.year = 2012
a1.maker = "MAZDA"
a1.power = "150 л.с."
a1.color = "red"
a1.price = 123456
a1.print_info()
