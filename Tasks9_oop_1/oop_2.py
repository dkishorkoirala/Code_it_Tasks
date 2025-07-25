class Student:
    def __init__(self, name, grade="Not Assigned"):
        self.name = name
        self.grade = grade

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")


s1 = Student("Ram")
s1.show_details()

s2 = Student("Hari", "A")
s2.show_details()
