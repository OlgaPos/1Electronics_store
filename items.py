class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity, discount_price=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount_price = discount_price

        self.all.append(self)

    def calculate_total_price(self):
        return self.price * self. quantity

    def apply_discount(self):
        self.discount_price = self.price * self.pay_rate


item1 = Item("Smartphone", 10000, 20)
item2 = Item("Laptop", 20000, 5)

print(item1.name)
print(item1.price)
print(item1.calculate_total_price())

item1.apply_discount()
print(item1.discount_price)
Item.pay_rate = 0.8
item1.apply_discount()
print(item1.discount_price)

print(item2.name)
print(item2.price)
print(item2.calculate_total_price())
print(item2.price)
print(Item.all)
