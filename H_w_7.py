class Student:
    def __init__(self, name):
        self.name = name
        self.lp = self.Laptop()

    def print_info(self):
        print(self.name, "=>", self.lp.show())

    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.ozu = "16"

        def show(self):
            return f"{self.model}, {self.cpu}, {self.ozu}"


s1 = Student("Roman")
s1.print_info()
s2 = Student("Vladimir")
s2.print_info()