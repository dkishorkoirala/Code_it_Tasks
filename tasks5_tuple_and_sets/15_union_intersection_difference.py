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

print(f"The union of set is {my_set.union(my_setb)}")

print(f"The intersenction of sets are {my_set.intersection(my_setb)}")

print(f"The difference of set a to b is {my_set.difference(my_setb)}")
print(f"The difference of set b to a is {my_setb.difference(my_set)}")
