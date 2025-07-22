MENU = '''
1. Add task
2. View all tasks
3. Remove task
4. Exit
'''
tasks = []

while True:
    print(MENU)
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"The task {task} has been added successfully....")
    
    elif choice == '2':
        print(tasks)
    
    elif choice == '3':
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"The task {task} has been removed successfully....")
        else:
            print("Task not found")
        
    elif choice == '4':
        print("Exiting the program....")
        break
    
    else:
        print("Invalid choice! Please Try again")
        