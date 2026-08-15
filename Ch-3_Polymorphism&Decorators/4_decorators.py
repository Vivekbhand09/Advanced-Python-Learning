# Without decorator

# Suppose you have 3 functions:
# def function1():
#     print("Starting")
#     print("Doing function 1")
#     print("Ending")


# def function2():
#     print("Starting")
#     print("Doing function 2")
#     print("Ending")


# def function3():
#     print("Starting")
#     print("Doing function 3")
#     print("Ending")

# You are repeating:

# print("Starting")
# print("Ending")

# This is where a decorator helps.

#------------------------------------------------------------------------------------------------------------------
# Decorator
def my_decorator(func):

    def wrapper():

        print("Starting")

        func()

        print("Ending")

    return wrapper


@my_decorator
def function1():
    print("Doing function 1")


@my_decorator
def function2():
    print("Doing function 2")


@my_decorator
def function3():
    print("Doing function 3")


# Calling the functions
function1()
function2()
function3()


# OUTPUT:
# Starting
# Doing function 1
# Ending
#
# Starting
# Doing function 2
# Ending
#
# Starting
# Doing function 3
# Ending