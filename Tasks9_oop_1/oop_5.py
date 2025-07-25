class School:
    school_name = "ABC Public School"

    def __init__(self, student_name):
        self.name = student_name

    def get_student_info(self):
        print(f"Name: {self.name}")
        print(f"School: {self.school_name}")

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        print(f"New School name = {cls.school_name}")


s1 = School("Ram")
s1.get_student_info()

s2 = School("hari")
# s2.change_school_name("XYZ School")
# School.change_school_name("XYZ School")
s2.get_student_info()
