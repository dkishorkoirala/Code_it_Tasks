# q3


def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func()

    return wrapper


@log_call
def say_hello():
    print("hello")


say_hello()
