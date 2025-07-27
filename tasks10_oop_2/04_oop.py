class ShoppingCart:
    def __init__(self, customer_name, cart=[]):
        self.customer_name = customer_name
        self.cart = cart

    def add_item(self, item):
        self.cart.append(item)

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
        else:
            print(f"Item '{item}' not found in cart")

    def view_cart(self):
        return self.cart


s1 = ShoppingCart("Ram")
s1.add_item("Laptop")
s1.add_item("Mobile")
s1.add_item("Tablet")


print(s1.view_cart())
s1.remove_item("Laptop")

print(s1.view_cart())
s1.remove_item("man")
