student1 = {
    "name": "ram",
    "age": "23"
}

student2 = {
    "grade": "A",
    "Roll_no": 23
}

student3 = student1.copy()
student3.update(student2)
print(student3)