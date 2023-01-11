import random


class Dog:
    name = "No name"
    age = 0
    lst = []

    def __init__(self, name: str, sex: str):
        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой")
        if not isinstance(sex, str):
            raise ValueError("Пол должен быть строкой")
        self.name = name
        self.sex = sex

    def print_info_dog(self):
        if self.sex == "M":
            return f"{self.name} is good boy!!!"
        elif self.sex == "F":
            return f"{self.name} is good girl!!!"
        else:
            raise ValueError("Пол необходимо вводите в формате 'M' или 'F'")

    @staticmethod
    def print_info_children():
        return Dog.lst

    def __add__(self, other):
        lst_sex = ["M", "F"]
        if self.sex != other.sex:
            for i in range(random.randint(1, 5)):
                Dog.lst.extend((f"{Dog.__name__}(name={Dog.name}", f"age={Dog.age}", f"sex={random.choice(lst_sex)})"))
            return Dog(self.name, self.sex + other.name + other.sex)
        raise AttributeError("Пол должен быть разный!")


dog1 = Dog("Tom", "M")
dog2 = Dog("Elsa", "F")
dog3 = dog1 + dog2
print(dog1.print_info_dog())
print(dog2.print_info_dog())
print(dog3.print_info_children())
