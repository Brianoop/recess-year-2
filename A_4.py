# Functions
# 1. allow for reusable code
# 2. allow for cleaner code
# 3. allow for testing
# 4. allow for debugging
# 5. allow for organization

# Syntax

# def function_name():
#     # code block
#     # code block

# function_name() call the function


def function_name():
    # print("Afternoon Session. Reccess")
    pass

function_name()

# function with parameters
# Parameter: is the variable listed inside the parentheses in 
# the function definition
def function_name(name) -> int:
    # print("Hello " + name)    
    pass

# Arg: is the value passed to the function
function_name("Overloaded function")


def add_multiple_numbers(*args):
    sum = 0
    for number in args:
        sum += number
    # print(sum)


add_multiple_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# using default parameters
def greetings(name = "BRIAN"):
    # print("Hello " + name)
    pass # do nothing


greetings() # defaults to BRIAN
greetings("Angoda") # overrides the default value


# Return a String value
def return_string_value():
    return "Hello World"


# Return a Integer value
def return_integer_value():
    return 100


# Return a Float value
def return_float_value():
    return 100.00


# Return a Boolean value
def return_boolean_value():
    return True


# Return a List value
def return_list_value():
    return [1, "Me", 3, 4, 5]



# Modules
# A module is a file containing a set of 
# functions to include in your application

# import the module
# math is a built-in module
import math

# use the module
# print(math.pi)

def product(x, y):
    return x * y

# print(product(2, 3))


# import everything from the file
# from python_modules import * # import all

# # import specific functions
# from python_modules import add_two_numbers, subtract_two_numbers 

# use as if there is a conflict
import python_modules as pm # pm is the alias. 

def display_numbers(number1, number2):
    # print(f"Printed from current file: {number1} and {number2}")
    pass

display_numbers(1, 2)
pm.display_numbers(1, 2)
# print(pm.add_two_numbers(1, 2))
# print(pm.subtract_two_numbers(1, 2))
# print(pm.multiply_two_numbers(1, 2))
# print(pm.divide_two_numbers(1, 2))


# cude root of a number
def cube_root(number):
    return math.pow(number, 1/3)

# print(cube_root(27))


# input & output in python

# input() function
# input is taken as a string

# name = input("Enter your name: ")
# print("Hello " + name)

# output
# print() function  
# print("Hello World")


# multiple input values on the same line
# name, age = map(str, input("Enter your name and age: ").split())
# print(name)
# print(age)

my_list = list(map(str, input("Enter your fav movies: ").split()))
# map function takes two arguments. 
# the map function is used to convert the input to a specific data type
# 1. the data type you want to convert to
# 2. the input() function
# split() function splits the input into a list

print(my_list)

my_set = set(map(str, input("Enter your fav artists: ").split()))
print(my_set)

