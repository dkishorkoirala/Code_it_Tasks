class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return f"Temperature in Fahrenheit: {round(self.celsius * 9 / 5, 2) + 32} °F"

    def to_kelvin(self):
        return f"Temperature in Kelvin: {round(self.celsius + 273.15, 2)} °K"


t1 = Temperature(25)
print(t1.to_fahrenheit())
print(t1.to_kelvin())
