def even_squares(lst):
    for num in lst:
        if num % 2 == 0:
            yield num**2


numbers = [1, 2, 3, 4, 5, 6]
gen = even_squares(numbers)

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
