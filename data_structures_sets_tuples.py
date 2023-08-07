# Complex numbers
x = 3j

# print(type(x))

# Lists
# A list is a collection which is ordered and changeable.
# In Python lists are written with square brackets.

# Accessing a range of items using the slice operator
listOfStrings = "Strings are immutable"
anotherListOfStrings = "Strings are immutable"
# print(listOfStrings[1:])
# print(listOfStrings[:1])
# print(listOfStrings[-1:])
# print(listOfStrings[:-1])
# print(listOfStrings[:])

# Create a list
myList = ["apple", "banana", "cherry", 2, 3, 5,
          {
              "name": "Angoda Brian Nyanga",
              "age": 29,
          }, True, None, 3j]

# print(myList[-4]['name'])

# newMergedList = listOfStrings + myList # - Type Error

newMergedList = listOfStrings + anotherListOfStrings # Have to be of the same type to be merged

# print(newMergedList)

myList.append("Nio Nio") # Add an item to the end of the list
myList.insert(0, "New World Order") # Add item to specified index
myList.pop(3) # Remove item at specific index

# print(myList)

# Tuples - Immutable - Cannot be changed. Use round brackets. Ordered

aTuple = ("apple", "banana", "cherry", 2, 3, 5,)
# aTuple = ("apple") # Add a comma to make it a tuple
# print(aTuple)
# aTuple[0] = "New Apple" # TypeError: 'tuple' object does not support item assignment
# aTuple.append("New Apple") # AttributeError: 'tuple' object has no attribute 'append'
# aTuple.insert(0, "New World Order") # AttributeError: 'tuple' object has no attribute 'insert'
# aTuple.pop(3) # AttributeError: 'tuple' object has no attribute 'pop'
# aTuple.remove("apple") # AttributeError: 'tuple' object has no attribute 'remove'
# aTuple.__add__("New Apple") # AttributeError: 'tuple' object has no attribute '__add__'

newTuple = list(aTuple)

newTuple.insert(0, "New World Order")

newTuple = tuple(newTuple)

# print(newTuple)
# print(type(newTuple))

# for loop in tuples
# for item in newTuple:
#     print(item)

# Sets - Mutable - Can be changed. Use curly brackets. Unordered

aSet = {"apple", "banana", "cherry", 2, 3, 5,}
# print(aSet)
# aSet.add("New Apple") # No effect if item already present
# print(aSet)
# aSet.update(["New World Order", "New World Order 2"]) # Add multiple items to the set
# print(aSet)
# aSet.remove("New World Order") # Raises an error if item not present in the set - KeyError: 'New World Order'
# print(aSet)
# aSet.discard("New World Order 2") # Does not raise an error if item not present in the set
# print(aSet)
# aSet.pop() # Remove a random item from the set
# print(aSet)
# aSet.clear() # Remove all items from the set
# print(aSet)



# ASSIGNEMT ONE

set1 = {"apple", "banana", "cherry", 2, 3, 5,}
set2 = {"New World Order", "New World Order 2"}
# Find the length of your set
print(len(set1))
# Find the data type of your set
print(type(set1))
# accessing items in a set. Access can not be done with an index or key because sets are unordered
for item in set1:
    print(item)
# add items to a set
set1.add("New Apple")
print(set1)
# add two sets together
set1.update(set2)
print(set1)

# recessassignments@gmail.com
# 0703832978
# Read about dicts, Strings, ...