# Author: Angoda Brian Nyanga
# Session: Afternoon

# Dictionaries
# 1. key-value. 2. key is unique. 3. key is immutable. Ordered. value is mutable. value can be duplicated
example = {
    "name": "Angoda Brian Nyanga",
    "age": 29,
}

print(example.keys())

# int, floats, complex numbers
# ints, floats & strings support python casting

# x = int(2.0) + str(2) + float(3)
# print(x) # Type Error

print("#" * 80)
print("# 1. Exercise. Return a list of all values in a dictionary")
print("#" * 80)

dictionary = {
    5: "Five",
    4: "Four",
    3: "Three",
    2: "Two",
    1: "One"
}

print(dictionary.values())
print("\n")

print("#" * 80)
print("# 2. Exercise. Check if a key does exist in your dictionary")
print("#" * 80)

entered_key = input("Enter a key: ")
try: 
    entered_key = int(entered_key)    
except ValueError as error: 
    print("Key must be a number")

my_key = dictionary.get(entered_key, -1)
if my_key == -1:
    print(f"The key {entered_key} does not exist in the dictionary")
else:
    print(f"The key {entered_key} exists in the dictionary")
print("\n")

print("#" * 80)
print("# 3. Exercise. How to change dictionary items. How to update items.")
print("#" * 80)

dictionary[5] = "Taano wange"
# dictionary.get(2) = "Bili" # This is wrong
print(dictionary)
print("\n")

print("#" * 80)
print("# 4. Exercise. How to add dictionary items. How to remove items.")
print("#" * 80)
# Add
dictionary.update({
    6: "Mukaaga"
})
print(dictionary)
# Remove
dictionary.popitem() # The popitem() method removes the item that was last inserted into the dictionary
print(dictionary)
print("\n")

print("#" * 80)
print("# 5. Exercise. How to loop through a dictionary. How to nest a dictionary.")
print("#" * 80)

# Loop through a dictionary
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")

# Nest a dictionary
nested_dictionary = {
    "name": "Angoda Brian Nyanga",
    "age": 29,
    "children": {
        "child1": {
            "name": "Angoda Jr.",
            "age": 5
        },
        "child2": {
            "name": "Angoda Jr. Jr.",
            "age": 3
        }
    }
}
print(nested_dictionary)
print("\n")

print("#" * 80)
print("# 6. Exercise. Determine the length of a string using the len() function.")
print("#" * 80)

my_string = "Hello World"
print(len(my_string))
print("\n")

print("#" * 80)
print("# 7. Exercise. Iterate through each character in a string using a for loop.")
print("#" * 80)

for character in my_string:
    print(character)
print("\n")

print("#" * 80)
print("# 8. Exercise. Slice a string to extract specific portions of it.")
print("#" * 80)

print(my_string[0:5]) # prints the characters from index 0 to 4
print("\n")

print("#" * 80)
print("# 9. Exercise. Perform arithmetic operations with numbers and print the results.")
print("#" * 80)

print(2 + 2) # Addition
print(2 - 2) # Subtraction
print(2 * 2) # Multiplication
print(2 / 2) # Division
print(2 % 2) # Modulus
print(2 ** 2) # 2 to the power of 2
print("\n")

print("#" * 80)
print("# 10. Exercise. Use boolean values and conditions to control program flow.")
print("#" * 80)

if 2 == 2:
    print("2 is equal to 2")
else:
    print("2 is not equal to 2")
print("\n")
