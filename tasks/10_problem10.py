marks = int(input("Enter your marks: "))


if (90 < marks <= 100):
    print("Grade is A+")

elif (80 < marks <= 90):
    print("Grade is A")

elif (70 < marks <= 80):
    print("Grade is B+")

elif (60 < marks <= 70):
    print("Grade is B")

elif (50 < marks <= 60):
    print("Grade is C+")

elif (40 < marks <= 50):
    print("Grade is C")

elif (30 < marks <= 40):
    print("Grade is D+")

elif (marks < 40):
    print("Grade is F")

else:
    print("Invalid marks")
