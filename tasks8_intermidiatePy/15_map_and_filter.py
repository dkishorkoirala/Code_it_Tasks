a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(map(lambda x: x * 2, a))
print("Double is", b)

c = list(filter(lambda x: x <= 10, b))
print("Filtered", c)
