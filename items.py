class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def calculate_total_price(self):
        return self.price * self. quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price


item1 = Item("Smartphone", 10000, 20)
item2 = Item("Laptop", 20000, 5)

print(item1.name)
print(item1.price)
print(f"Общая стоимость смартфонов {item1.calculate_total_price()}")

Item.pay_rate = 0.8  # Устанавливаем новый уровень цен
item1.apply_discount()   # К цене смартфона применяем скидку
print(item1.price)

print(item2.name)
print(item2.price)
print(f"Общая стоимость ноутбуков {item2.calculate_total_price()}")
print(item2.price)
print(Item.all)
