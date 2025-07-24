def gene():
    for i in range(1, 101):
        yield i


obj = gene()
for i in obj:
    print(i)
