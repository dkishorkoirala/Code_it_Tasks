i = [1, 2,3,4,5,6,7,8,9,10]

for j in i:
    if j % 2 == 0:
        i.remove(j)

print(i)