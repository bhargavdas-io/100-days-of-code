import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        time.sleep(2)
        print("Hi, again")

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello from Seattle")


say_hello()


@delay_decorator
def say_night():
    print("Goodnight")


say_night()
