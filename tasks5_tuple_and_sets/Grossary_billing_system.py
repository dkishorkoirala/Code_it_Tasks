item_list = []

for i in range(5):
    item = input("Enter your item: ")
    item_list.append(item)

item_price = []

for i in range(5):
    price = int(input("Enter your price: "))
    item_price.append(price)

print(item_list)
print(item_price)

print("The total amount of bill you have to pay is:", sum(item_price))