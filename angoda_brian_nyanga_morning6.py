"""
Author: Angoda Brian Nyanga
Github repo: https://github.com/Brianoop/recess-year-2.git

DAY 6:
- REGEX
- GEnerators & Iterators
- Decorators
- Context Managers
- Multithreading & Multiprocessing
"""

# REGEX# Summary of Regular Expression Patterns
# /d - digit 0-9 (any digit) 
# /D - non-digit (any non-digit character)
# /s - whitespace (tab, space, newline, etc.)
# /S - non-whitespace (any non-whitespace character)
# /w - alphanumeric (any letter, digit, or underscore)
# /W - non-alphanumeric (any non-letter, digit, or underscore)
# /b - word boundary (between \w and \W)
# /B - non-word boundary
# /A - beginning of string
# /Z - end of string
# /z - end of string
# /G - end of previous match
# /n - backreference to group number "n"
# /c - matches any character or escape sequence that may be
#      treated like a character
# /Q - quote (disable) pattern metacharacters until /E
# /E - end quote (enable) pattern metacharacters after /Q
# /p{name} - matches the named group
# /P{name} - matches the named group
# /k<name> - backreference to named group
# /k'name' - backreference to named group
# /x - ignore whitespace and comments
# /i - case-insensitive matching
# /L - locale character classes
# /u - unicode character classes
# /8 - use ASCII rules
# /a - ASCII character classes
# /A - POSIX character classes (US-ASCII only)
# /u - unicode character classes
# /U - Unicode character properties
# /X - Unicode character properties
# .: any character except newline
# ^: start of string
# $: end of string
# *: match 0 or more repetitions
# +: match 1 or more repetitions
# ?: match 0 or 1 repetitions
# {m,n}: match m to n repetitions
# {m,n}?: match m to n repetitions, not greedily
# {m,}: match m or more repetitions
# {m,}?: match m or more repetitions, not greedily
# {m}: match exactly m repetitions
# {m}?: match exactly m repetitions, not greedily
# (?#...): comment
# (?:...): non-capturing group
# (?P<name>...): named capturing group
# (?P=name): backreference to named group
# (?=...): positive lookahead assertion
# (?!...): negative lookahead assertion
# (?<=...): positive lookbehind assertion
# (?<!...): negative lookbehind assertion
# (?(id/name)yes-pattern|no-pattern): conditional
# \number: backreference to group number "number"
# \A: start of string
# \b: word boundary
# \B: non-word boundary 
# [ ]: character set (any character in set)
# [^ ]: negated character set (any character except those in set)
# ^: start of string (or line, in multiline mode)
# $: end of string (or line, in multiline mode)


# Matching & Searching using regex
# Match firsst word with regex


import re
# re.match(pattern, string, flags=0)
name = "Wilfred Majaliwa M"
# Match first word
# \w+ - one or more word characters
match = re.match(r'(\w+)', name, re.I)
if match:
    # print("Match:", match.group())
    pass

# I - ignore case
# re.I - ignore case
matches = re.findall(r'(\w+) (\w+)', name, re.I)
if matches:
    # print("Findall:", matches)
    pass


# Validate email address using regex
def validate_email(email):
    # ^[a-zA-Z0-9_.+-] - start with any of these characters
    # + - one or more
    # @ - @ symbol
    # \. - dot
    # [a-zA-Z0-9-] - any of these characters
    # $ - end of string
    # pattern = xxxx@xxxx.xxxx
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(pattern, email)
    if match:
        return True
    return False

email_pass = "wilfredmajaliwa@gmail.com"
email_reject = "wilfredmajaliwa@gmail"

# print(validate_email(email_pass)) # True
# print(validate_email(email_reject)) # False


# Generators & Iterators
# Generators are functions that return an object that can be iterated over
# Generators use yield keyword instead of return
# Generators are memory efficient
# Generators are lazy
# Generators are used to create iterators
# Generators are used to create infinite sequences
# Generators are used to create data pipelines
# Generators are used to create data processing pipelines


# Create a generator
def my_generator():
    yield 1
    yield 2
    yield 3

# print(my_generator()) # <generator object my_generator at 0x7f9b1c0b6f20>
# print(next(my_generator())) # 1
# print(next(my_generator())) # 2
# print(next(my_generator())) # 3
# print(next(my_generator())) # StopIteration


# Create a function that returns the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Yield the factorial of a range of numbers from 0 to 10 using a generator
def factorial_generator(n, m):
    for i in range(n, m):
        # The yield keyword returns a generator object that can be iterated over
        yield f"The factorial of {i} is {factorial(i)}"
        
# Iterate over the generator object
for factorial_value in factorial_generator(1, 10):
    # print(factorial_value)
    pass


def squares(n, m):
    for i in range(n, m):
        yield f"The square of {i} is {i**2}"

# Create a generator object
squares_generator = squares(1, 6)

# Print the first 5 squares of numbers from 1 to 5
for square in squares_generator:
    # print(square)
    pass


# Decorators
# Decorators are functions that take another function as an argument
# Decorators add functionality to an existing function
# Decorators return another function
# Decorators are used to modify the behavior of a function
# Decorators are used to modify the behavior of a class

# Create a decorator function, my_decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator # Referring to the decorator function, my_decorator
# Extra functionality to add to the wrapper function
def say_hello():
    # This is the implementation to be added to the wrapper function
    print("Hello")

# say_hello() 
# Before function call
# Hello
# After function call


# ADVANCED PYTHON

# Context Manager
# Context manager is an object that defines a temporary context for the execution of a block of code

# Benefits of context managers
# 1. Resource management
# 2. Exception handling
# 3. Code simplification


# Example 1: Demonstrate a context manager to open a file and return a context manager instance

import contextlib

# Define the open_file as a context manager
@contextlib.contextmanager
# By using the @contextlib.contextmanager decorator, you don't need to define a separate class for the context manager. 
# The decorator takes care of creating the necessary class and implementing the context manager protocol for you.
def open_file(filename):
    file = open(filename, "r")

    try:
        # The yield statement is used to define the body of the __enter__ method
        # The yield statement acts as a placeholder for the code inside the with block
        # It allows the block to be executed, and then control is returned to the context manager to perform any necessary cleanup.
        yield file
    finally:
        # The finally block is used to define the body of the __exit__ method
        file.close()

# The with keyword is used to create a context manager
with open_file("data.txt") as file:
    contents = file.read()
    # print(contents) # Something blue

# A similar example using the contextlib.ContextDecorator class
# import contextlib // Don't wan to import the contextlib module again

# In this example, the OpenFile class inherits from the contextlib.ContextDecorator class, 
# which provides the necessary functionality for a context manager.
class OpenFile(contextlib.ContextDecorator):
    # The __init__ method initializes the OpenFile object with the provided filename attribute, 
    # which represents the file to be opened.
    def __init__(self, filename):
        self.filename = filename # Initialize the filename attribute
        self.file = None # Initialize the file object to None

    def __enter__(self):
        # The __enter__ method is called when entering the with block and opens the file. 
        # It returns the file object, allowing you to use it within the block.
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # The __exit__ method is called when exiting the with block. It is responsible for closing the file.
        self.file.close()

# The with keyword is used to create a context manager
# Using the OpenFile class as a context decorator allows you to use it directly with the with statement, 
# providing a clean and concise way to handle file operations within a context.
with OpenFile("data.txt") as file:
    contents = file.read()
    # print(contents) # Something blue


import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        # # This is why it prints the time taken even after commenting out the time.sleep(1) statement
        # because the __exit__ method is called when exiting the with block
        # print(f"Time taken: {self.interval} seconds") 


with Timer() as timer:
    # time.sleep(1) // Still prints the time taken even after commenting it out. TODO: Find out why
    pass



# MULTI-THREADING AND MULTI-PROCESSING
# Multi-threading is a technique that allows a program to perform multiple tasks concurrently within a single process
# Multi-processing is a technique that allows a program to use multiple cores of a CPU to perform multiple tasks concurrently


# Multi-threading
# Threads share the same memory space and can access the same data in memory concurrently.
# Threads are lightweight and require less memory overhead than processes.
import threading

def task(name):
    print(f"Task {name} has started")
    for i in range(10000000):
        pass
    print(f"Task {name} has completed")


# Create multiple threads
t1 = threading.Thread(target=task, args=("t1",))
t2 = threading.Thread(target=task, args=("t2",))


# Start the threads
# t1.start() # Task t1 has started
# t2.start() # Task t2 has started


# Wait for the threads to complete
# t1.join() # Task t1 has completed
# t2.join() # Task t2 has completed


# MULTI-PROCESSING
# Processes do not share the same memory space and cannot access the same data in memory concurrently.

# Demonstrate the use of the multiprocessing module to create multiple processes
import multiprocessing

def process_task(name):
    # print(f"Processing task {name}")
    pass
# The multiprocessing module spawns new processes by creating a new Python interpreter for each process. 
# This bootstrapping process involves importing the necessary modules and preparing the environment for the new process. 
# However, interactive environments, by default, already have an active Python interpreter running, 
# and attempting to start a new process conflicts with the ongoing bootstrapping phase.

# To resolve the RunTimeError issue, you can place your multiprocessing code inside the if __name__ == '__main__': block. 
# This condition ensures that the code is only executed when the script is run as the main module, 
# and not when it is imported as a module by another script or when running in an interactive environment.
"""
By enclosing the multiprocessing code within the if __name__ == '__main__': block, 
you ensure that the code is executed only when running the script directly, 
preventing conflicts with the bootstrapping process and resolving the RuntimeError."""
if __name__ == '__main__':
    # create a multiprocessing pool object with a specified number of worker processes
    pool = multiprocessing.Pool(processes=3)
    # processess is the number of worker processes to use. If processes is None then the number returned by os.cpu_count() is used.
    # The pool of worker processes will execute the tasks concurrently, and you can control the level of parallelism by adjusting 
    # the number of processes in the pool. In this case, with processes=3, at most three tasks will be executed concurrently.

    # submit multiple tasks to the pool
    for i in range(3):
        pool.apply_async(process_task, args=(f"Process {i}",))

    # close the pool and wait for the tasks to complete
    pool.close()
    pool.join()



# COMBINE MULTI-THREADING AND MULTI-PROCESSING
# Example:

# import the necessary modules
import threading, multiprocessing

# define a function for the task
def task(name):
    print(
        f"Task {name} running on process id {multiprocessing.current_process().pid}"
        f" with thread id {threading.get_ident()}"
        )


# create multiple threads
threads = []
for i in range(2):
    thread = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(thread)
    thread.start() # The results vary depending on the number of cores available on your machine.

# wait for the threads to complete
for thread in threads:
    thread.join()