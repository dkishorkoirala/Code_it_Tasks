marks = {
    # "subject" : "marks"
}

for i in range(5):
    subject = input("Enter subject name: ")
    mark = int(input("Enter the marks: "))
    marks[subject] = mark

for sub, mark in marks.items():
    total = sum(marks.values())
    avg = total / len(marks)
    print(f"{sub}: {mark}")

print("\nTotal marks is :",total)
print("Average marks is:",avg)