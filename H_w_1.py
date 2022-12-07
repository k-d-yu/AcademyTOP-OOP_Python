class Book:
    name = "название книги"
    year_of_release = "год выпуска"
    publisher = "издатель"
    genre = "жанр"
    author = "автор"
    price = "цена"

    def print_info(self):
        print("Информация о книге".upper().center(30, "_"))
        print(f"Название книги: {self.name}\nГод выпуска: {self.year_of_release}\nИздатель: {self.publisher}\n"
              f"Жанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}")
        print("_" * 30)

    def input_info(self, name, year_of_release, publisher, genre, author, price):
        self.name = name
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year_of_release(self, year_of_release):
        self.year_of_release = year_of_release

    def get_year_of_release(self):
        return self.year_of_release

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


b1 = Book()
b1.print_info()
b1.input_info("Евгений Онегин", "2022", "Азбука", "Роман в стихах", "Пушкин А.С.", "181 руб.")
b1.print_info()

b1.set_name("Вий")
print(b1.get_name())
b1.set_year_of_release("2022")
print(b1.get_year_of_release())
b1.set_publisher("Стрекоза")
print(b1.get_publisher())
b1.set_genre("Повесть")
print(b1.get_genre())
b1.set_author("Гоголь Н.В")
print(b1.get_author())
b1.set_price("334 руб.")
print(b1.get_price())