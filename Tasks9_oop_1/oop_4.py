class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


dog = Dog("Fido")
dog.show_details()
print(dog.species)
print(Dog.species)
