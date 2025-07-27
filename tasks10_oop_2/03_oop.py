class Employee:
    company_name = "TechSoft"

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company_name}")

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
        # print(f"New Company name = {cls.company_name}")


e1 = Employee("Ram", "manager", 50000)
e1.show_info()

e1.change_company("XYZ")
e1.show_info()
