math = int(input("Enter your marks in Math: "))
physics = int(input("Enter your marks in Physics: "))
chemistry = int(input("Enter your marks in Chemistry: "))

marks = (math, physics, chemistry)
marks_ = tuple(marks)  #this is not necessary but for clearity

print(f"The average of these three subs are: {sum(marks_)/len(marks_)}")