students =  {
    "Ram": [80, 85, 78], 
    "Sita": [90, 92, 88]
}

for student, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{student}: {avg}")