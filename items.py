import csv


class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: int, quantity: int):
        """Инициализируем класс"""
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)  # Не стоит добавлять внутрь экземпляра самого себя

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self) -> str:
        """Декоратор позволяет вносить изменения в private атрибут"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Проверяем, чтобы длина названия товара не была больше 10 букв"""
        if len(value) < 11:
            self.__name = value
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, path: str):
        """Принимаем список товаров из файла csv"""
        items = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                items.append(cls(row["name"], int(row["price"]), int(row["quantity"])))
            return items

    @staticmethod
    def is_integer(num) -> bool:
        """Проверяем, является ли число целым"""
        if num % 1 == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """Складываем количество товаров в классах Item и Phone"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Сложение возможно только для экземпляров классов Item и Phone")


class Phone(Item):

    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int):
        """Наследуем инициализацию класса Phone от Item. Доп. атрибут - количество сим-карт"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Наследуем метод repr от класса Item с доп. атрибутом количество сим-карт"""
        return f"{super().__repr__().replace(')', '')}, {self.__number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """Декоратор позволяет вносить изменения в private атрибут"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        """Проверяем, чтобы количество сим-карт было больше 0"""
        if value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError("Количество физических сим-карт должно быть целым числом больше нуля")


class Mixing:

    def __init__(self, *args):
        """Создаём специальный класс для хранения и изменения языка клавиатуры"""
        self.__language = 'EN'  # по умолчанию при инициализации 'EN'
        super().__init__(*args)

    @property
    def language(self) -> str:
        """Декоратор позволяет вносить изменения в private атрибут"""
        return self.__language

    def change_lang(self):
        """Метод для изменения раскладки клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class KeyBoard(Mixing, Item):

    def __init__(self, *args):
        """Наследуем инициализацию класса от Mixing и Item"""
        super().__init__(*args)


if __name__ == '__main__':
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    # print(KeyBoard.__mro__)
    print(kb)
    print(kb.language)
    kb.change_lang()
    print(kb.language)
    kb.language = 'CH'

    # смартфон iPhone 14, цена 120_000, количество товара 5, сим-карт 2
    # phone1 = Phone("iPhone 14", 120_000, 5, 2)
    # print(phone1)
    #
    # print(repr(phone1))

    # phone1.number_of_sim = 0

    # item1 = Item("Смартфон", 10000, 20)
    # item1
    # Item('Смартфон', 10000, 20)
    # print(item1)

    # item3 = Item('Phone', 10000, 5)
    # item3.name = "Smartphone"
    # print(item3.name)
    # item3.name = "SuperSmartphone"

    # Item.instantiate_from_csv('data/items.csv')  # создание объектов из данных файла
    # print(len(Item.all))  # в файле 5 записей с данными по товарам
    # item1 = Item.all[0]
    # print(item1.name)
    #
    # print(Item.is_integer(5))
    # print(Item.is_integer(5.0))
    # print(Item.is_integer(5.5))

    # item1 = Item("Smartphone", 10000, 20)
    # item2 = Item("Laptop", 20000, 5)

    # print(item1.name)
    # print(item1.price)
    # print(f"Общая стоимость смартфонов {item1.calculate_total_price()}")
    #
    # Item.pay_rate = 0.8  # Устанавливаем новый уровень цен
    # item1.apply_discount()   # К цене смартфона применяем скидку
    # print(item1.price)
    #
    # print(item2.name)
    # print(item2.price)
    # print(f"Общая стоимость ноутбуков {item2.calculate_total_price()}")
    # print(item2.price)
    # print(Item.all)
