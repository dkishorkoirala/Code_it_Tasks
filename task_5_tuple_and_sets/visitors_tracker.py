visitors_names = set()

a = input("Are you a visitor(y/n): ")

while a.lower() == "y":
    name = input("Enter your name: ")
    visitors_names.add(name)
    a = input("Are you a visitor(y/n): ")



print(f"Total number of visitors: {len(visitors_names)}")
print(visitors_names)