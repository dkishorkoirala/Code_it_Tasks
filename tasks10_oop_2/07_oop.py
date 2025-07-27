class Book:
    discount_percentage = 0

    def __init__(self, price):
        self.price = price

    @classmethod
    def set_discount(cls, percentage):
        cls.discount_percentage = percentage / 100

    def price_after_discount(self):
        return self.price - (self.price * self.discount_percentage)


b1 = Book(1000)
b1.set_discount(10)
print(b1.price_after_discount())
