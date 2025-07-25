class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("The sum of two numbers is:", self.a + self.b)

    def subtract(self):
        print("The difference of two numbers is:", self.a - self.b)

    def multiply(self):
        print("The product of two numbers is:", self.a * self.b)

    def divide(self):
        try:
            result = self.a / self.b
        except ZeroDivisionError:
            print("Cannot divide by zero!!")

        else:
            print("The division of two numbers is:", result)


c1 = Calculator(1, 0)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()

c2 = Calculator(2, 4)
c2.add()
c2.subtract()
c2.multiply()
c2.divide()
