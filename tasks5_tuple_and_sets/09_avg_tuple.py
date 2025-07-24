list_ = []
for i in range(5):
    num = int(input("Enter a number: "))
    list_.append(num)

myTuple = tuple(list_)
print(f"The average of tuple is {sum(myTuple)/len(myTuple)}")