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
        return self.price * self. quantity

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


if __name__ == '__main__':
    # item3 = Item('Phone', 10000, 5)
    # item3.name = "Smartphone"
    # print(item3.name)
    # item3.name = "SuperSmartphone"

    Item.instantiate_from_csv('data/items.csv')  # создание объектов из данных файла
    print(len(Item.all))  # в файле 5 записей с данными по товарам
    item1 = Item.all[0]
    print(item1.name)

    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))

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
