# Author: Angoda Brian Nyanga
# Date: 2023-07-01
# Description: Exception Handling & File Handling
# Session: Afternoon
# Github: https://github.com/Brianoop/recess-year-2.git
# Assignment: 5

# An Exception is an error that happens during execution of a program.
# When that error occurs, Python generate an Exception that can be handled
# Which avoids your program to crash.

# Three types of errors can occur in a Python program:
# 1. Syntax errors
# 2. Logical errors
# 3. Runtime errors


# Exception Handling With Try & Except
import traceback


print("#" * 80)
print("Exception Handling With Try & Except")
number = input("Enter a number: ")
try:  
    # This code will run if the input is a number
    number = int(number)
    print(number)
except ValueError as err:
    # This code will run if the input is not a number
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")
print("#" * 80)
print("\n")

# Exception Handling using raise
print("#" * 80)
print("Exception Handling using raise")
number = input("Enter a number: ")
try:
    number = int(number)
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    print(number)
except ValueError as err:
    print("Invalid input. Please enter a number")
    print(f"Error: {err}")
print("#" * 80)
print("\n")

# Exception Handling using assert
print("#" * 80)
print("Exception Handling using assert")
number = input("Enter a number: ")
try:
    number = int(number)
    # The assert keyword lets you test if a condition in your code returns True, 
    # if not, the program will raise an AssertionError.
    assert number >= 0 
    # OR assert number >= 0, "Negative numbers are not allowed" 
    # prints "Negative numbers are not allowed" if the number is negative and the traceback
    print(number)
except AssertionError as err:
    print("Invalid input. Please enter a number")
    # traceback.print_exc() prints the traceback of the error
    # import traceback
    traceback.print_exc()
    # Standard assert statement doesn't put anything into the AssertionError, 
    # it's the traceback that matters
    print(f"Error: {err}")
print("#" * 80)
print("\n")

# Exception Handling using else
print("#" * 80)
print("Exception Handling using else")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
else:
    # This code will run if the input is a number
    print(number)
print("#" * 80)
print("\n")

# Exception Handling using finally
print("#" * 80)
print("Exception Handling using finally")
number = input("Enter a number: ")
try:
    number = int(number)
    # This syntaxt will print the traceback of the error if the input is negative
    # And the AssertionError will be raised as "Negative numbers are not allowed"
    assert number >= 0, "Negative numbers are not allowed"
finally:
    # This code will always run
    print(number)
    print("This code will always run")
print("#" * 80)
print("\n")


# Multiple except clauses
print("#" * 80)
print("Multiple except clauses")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except AssertionError:
    print("Invalid input. Please enter a number")
except ValueError:
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")


# Exceptions as a tuple in a single except clause
print("#" * 80)
print("Exceptions as a tuple in a single except clause")
number = input("Enter a number: ")
try:
    number = int(number)
    assert number >= 0
except (AssertionError, ValueError):
    print("Invalid input. Please enter a number")
else:
    print(number)
print("#" * 80)
print("\n")



# File Handling 
# Python has several functions for creating, reading, updating, and deleting files.
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# create a file called demofile.txt with the contents "This is a demo file"
print("#" * 80)
print("create a file with its contents")
filename = input("Enter a filename: ")
extension = input("Enter the extension of the file: (e.g txt, py, html etc) ")
contents = input("Enter the contents of the file: ")

f = open(f"{filename}.{extension}", "w")
f.write(contents)
f.close()
print("#" * 80)
print("\n")

# To open a file for reading it is enough to specify the name of the file:
print("#" * 80)
print("To open a file for reading it is enough to specify the name of the file:")
print(f"Opening the file {filename}.{extension}...")
f = open(f"{filename}.{extension}")
print("Reading its contents...")
print(f.read())
print("#" * 80)
print("\n")

# Read Only Parts of the File
print("#" * 80)
print("Read Only Parts of the File")
f = open(f"{filename}.{extension}", "r")
print("Reading the first 5 characters...")
print(f.read(5))
print("#" * 80)
print("\n")

# Read Lines
print("#" * 80)
print("Read Lines")
f = open(f"{filename}.{extension}", "r")
print("Reading the first line...")
print(f.readline())
print("#" * 80)
print("\n")

# Close Files
print("#" * 80)
print("Close Files")
f = open(f"{filename}.{extension}", "r")
print("Closing the file...")
print(f.readline())
f.close()
print("#" * 80)
print("\n")

# Write to an Existing File
print("#" * 80)
print("Write to an Existing file")
extra = input(f"Add extra content to the file {filename}.{extension}: ")
f = open(f"{filename}.{extension}", "a")
f.write(extra)
f.close()
#open and read the file after the appending:
print("Opening and reading the file after appending...")
f = open(f"{filename}.{extension}", "r")
print(f.read())
f.close()
print("#" * 80)
print("\n")

# Overwrite the content
print("#" * 80)
print("Overwrite the content")
print("Opening and reading the file before overwriting...")
y_n = input(f"Do you wish to overwrite {filename}.{extension}? y/n: ")
if y_n == "y":
    # only open if you wish to overwite otherwise, file becomes empty
    f = open(f"{filename}.{extension}", "w")
    f.write("Woops! I have overwritten the content!")
else:
    print(f"{filename}.{extension} not overwritten")
f.close()
print("\n")

#open and read the file after the overwriting:
print("#" * 80)
print("open and read the file after attempted overwrite:")
f = open(f"{filename}.{extension}", "r")
print(f.read())
print("#" * 80)
print("\n")

# Create a New File
print("#" * 80)
new_filename = input("Create a New File: ")
its_extension = input("Enter the extension of the file: (e.g txt, py, html etc) ")
open(f"{new_filename}.{its_extension}", "x")
print("#" * 80)
print("\n")

# Delete a File
print("#" * 80)
print("Delete a File")
import os
filename_to_delete = input("Enter the filename to delete including its extension: ")
os.remove(f"{filename_to_delete}")
print("#" * 80)
print("\n")

# Check if File exist
print("#" * 80)
print("Check if the deleted file exist")
check_file = input("Enter the filename and its extension to check for it: ")
import os
if os.path.exists(f"{check_file}"):
    os.remove(f"{check_file}")
    print(f"{check_file} has been deleted successfully")
else:
    print("The file does not exist")
print("#" * 80)
print("\n")

# create a folder called myfolder
print("#" * 80)
print("create a folder called my_folder")
new_folder = input("Enter the name of the folder to create: ")
import os
os.mkdir(f"{new_folder}")
print("#" * 80)
print("\n")

# Delete Folder
print("#" * 80)
print("Delete Folder")
delete_folder = input("Enter the name of the folder to delete: ")
import os
os.rmdir(f"{delete_folder}")
print("#" * 80)
print("\n")

# Read a file using with
print("#" * 80)
print("Read a file using with")
read_file = input("Enter the name of the file to read: (include its extension) ")
if os.path.exists(read_file):
    with open(f"{read_file}", "r") as f:
        print(f"Reading {read_file}...")
        print(f.read())
else:
    print(f"{read_file} does not exist")
print("#" * 80)
print("\n")

# Write to a file using with
print("#" * 80)
print("Write to a file using with")
write_to_file = input("Enter the name of the file to write to: (include its extension). Careful as this will overwrite any content in that file. ")
if os.path.exists(write_to_file):
    overwrite = input(f"Enter the content to overwrite {write_to_file} with: ")
    user_concent = input(f"Do you wish to overwrite {write_to_file}? y/n: ")
    if user_concent == "y":
        # only open if you wish to overwite otherwise, file becomes empty
        with open(f"{write_to_file}", "w") as f:
            f.write(overwrite)
    else:
        print(f"{write_to_file} not overwritten")
else:
    print(f"{write_to_file} does not exist")
print("#" * 80)
print("\n")


# Using a main function, 
# create a program that will create a file myfile.txt, 
# add the content "Hello World" to the file, and then print the content of the file.
# The file should be created in the same directory as the program and use exception handling.
print("#" * 80)
print(
    """
    Using a main function, create a program that will create a file myfile.txt, 
    add the content Hello World to the file, and then print the content of the file. 
    The file should be created in the same directory as the program and use exception handling.
      """)
def main():
    myfile = input("Enter the filename and its extension: ")
    myfile_content = input("Enter the content for the file: ")
    try:
        with open(f"{myfile}", "x") as f:
            f.write(f"{myfile_content}")
            f.close()
    except FileExistsError:
        print("The file already exists")
    with open(f"{myfile}", "r") as f:
        print(f.read())
        f.close()


if __name__ == "__main__":
    main()
print("#" * 80)
print("\n")


print("\n")
print("*" * 80)
print("Congratulations!! You've reached the end of the program.")
print("*" * 80)