def only_even_args(func):
    def wrapper(*args):
        for arg in args:
            if arg % 2 != 0:
                print("Even number only ")
                return
        return func(*args)

    return wrapper


@only_even_args
def nums(*nums):
    print("Even numbers")


nums(1, 2, 3, 4)
nums(2, 4, 6, 8)
