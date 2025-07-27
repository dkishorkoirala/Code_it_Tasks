class SchoolStudent:
    def __init__(self, name, class_name, marks={}):
        self.name = name
        self.class_name = class_name
        self.marks = marks

    def add_marks(self, subject, score):
        self.marks[subject] = score
        return f"Marks for {subject} added successfully"

    def average(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)


s1 = SchoolStudent("Ram", 10)
s1.add_marks("Maths", 80)
s1.add_marks("Science", 90)
s1.add_marks("COmputer", 50)

print(s1.marks)
print(s1.average())
