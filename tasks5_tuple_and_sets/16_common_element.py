my_set = set()
# print(type(my_set))

for i in range(5):
    num = int(input("Enter a number for set A: "))
    my_set.add(num)
# print(my_set)

my_setb = set()
# print(type(my_set))

for i in range(5):
    num = int(input("Enter a number for set B: "))
    my_setb.add(num)
# print(my_setb)
print(f"The common elements of sets are {my_set.intersection(my_setb)}")
