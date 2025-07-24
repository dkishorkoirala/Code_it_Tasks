import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"{func.__name__} took {time_taken:.2f} seconds")

    return wrapper


@measure_time
def task():
    time.sleep(5)
    print("Task is completed")


task()
