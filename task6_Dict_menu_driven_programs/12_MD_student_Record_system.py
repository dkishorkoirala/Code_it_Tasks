MENU = '''
1. Add student
2. Delete student
3. View all students
4. Exit
'''
students = { "name" : "roll_no",}

while True:
    print(MENU)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter student roll no: ")
        students[name] = roll_no
        print(f"The student {name} with roll no {roll_no} has been added successfully....")
        
    elif choice == "2":
        name = input("Enter student name to delete: ")
        del students[name]
        print(f"The student {name} has been deleted successfully....")
    elif choice == "3":
        print(students)
    elif choice == "4":
        print("Exiting the program....")
        break
    else:
        print("Invalid choice! Please Try again")