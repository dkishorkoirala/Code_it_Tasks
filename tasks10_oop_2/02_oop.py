import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area: {round(math.pi * self.radius**2, 2)}"

    def circumference(self):
        return f"Circumference: {round(2 * math.pi * self.radius, 2)}"


c1 = Circle(5)
print(c1.area())
print(c1.circumference())
