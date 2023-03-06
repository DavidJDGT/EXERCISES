"""Create a decorator that measures the execution time of a function,
The decorator should print the time the function takes to execute."""

import time

def time_it (func):

    def wrapper(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        finish = time.time()
        print(f"Execute time {finish - start} seconds.")
        return result
    return wrapper


@time_it
def greet():

    n = input("Write your name: ")
    return f"hello {n}"

greet()