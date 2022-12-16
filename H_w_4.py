# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(val, rate):
#         return val * rate
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return f"__Изменение владельца__: {self.__surname}"
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return f"__Изменение баланса__: {self.__value}"
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_percent(self):
#         return f"__Изменение процента__: {self.__percent}"
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return f"__Изменение счета__: {self.__num}"
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято.")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_used(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}.")
#
#     def print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_info()
# acc.convert_to_used()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# acc.convert_to_used()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# Account.rate_usd = 600
# acc.set_surname("Дюма")
# print(acc.get_surname())
# acc.set_value(10000)
# print(acc.get_value())
# acc.set_percent(0.3)
# print(acc.get_percent())
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(30000)
# print()
# acc.withdraw_money(1000)
# print()
# acc.add_money(50000)
# print()
# acc.withdraw_money(30000)
# print()
# acc.set_num("54321")
# print(acc.get_num())
######################################################################################################################

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(val, rate):
        return val * rate

    @property
    def surname(self):
        return f"__Изменение владельца__: {self.__surname}"

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def value(self):
        return f"__Изменение баланса__: {self.__value}"

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def percent(self):
        return f"__Изменение процента__: {self.__percent}"

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @property
    def num(self):
        return f"__Изменение счета__: {self.__num}"

    @num.setter
    def num(self, num):
        self.__num = num

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снято.")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def convert_to_used(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}.")

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)


acc = Account("12345", "Долгих", 0.03, 1000)
acc.print_info()
acc.convert_to_used()
acc.convert_to_eur()

Account.set_usd_rate(2)
acc.convert_to_used()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()
Account.rate_usd = 600
acc.surname = "Дюма"
print(acc.surname)
acc.value = 10000
print(acc.value)
acc.percent = 0.3
print(acc.percent)
acc.print_info()
acc.add_percents()
print()
acc.withdraw_money(30000)
print()
acc.withdraw_money(1000)
print()
acc.add_money(50000)
print()
acc.withdraw_money(30000)
print()
acc.num = "54321"
print(acc.num)
