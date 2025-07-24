MENU = '''
1. Add book
2. Issue book
3. Return book
4. Display books
5. Exit
'''
library = {}

while True:
    print(MENU)
    choice = input("Enter your choice: ")
    
    if choice == "1":
        book_name = input("Enter book name: ")
        library[book_name] = True
        print(f"The book {book_name} has been added successfully....")
        
    elif choice == "2":
        book_name = input("Enter book name to issue: ")
        if book_name in library:
            library[book_name] = False
            print(f"The book {book_name} has been issued successfully....")
        else:
            print("Book not found")
        
    elif choice == "3":
        book_name = input("Enter book name to return: ")
        if book_name in library:
            library[book_name] = True
            print(f"The book {book_name} has been returned successfully....")
        else:
            print("Book not found")
        
    elif choice == "4":
        print(library)
        
    elif choice == "5":
        print("Exiting the program.....")
        break
    else:
        print("Invalid choice! Please Try again")