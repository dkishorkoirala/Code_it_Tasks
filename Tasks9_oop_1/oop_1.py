class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


b1 = Book("The alchemist", "Paulo Coelho", 1988)
b2 = Book("Rich Dad and Poor Dad", "Robert Kiyosaki", 2007)

b1.show_details()
b2.show_details()
