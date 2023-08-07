
# LISTS

# 1. Create a list with 5 items (names of people) 
# and write a python program to output the 2nd item.
first_list = ["Bezos", "Mark", "Elon", "Smith", "Tate"]
second_item = first_list[1]
print(second_item)

# 2. Write a python program to change the value of the first item to a new value
first_item = first_list[0]
first_item = "Wil"
print(first_item)

# 3. Write a python program to add a sixth item to the first_list
sixth_item = first_list.append("Jada")
print(first_list)

# 4. Write a python program to add “Bathel” as the 3rd item in your first_list
first_list[2] = "Bathel"
print(first_list)

#5.  Write a python program to remove the 4th item from the first_list
fourth_item = first_list[3]
first_list.remove(fourth_item)
print(first_list)

# 6. Use negative indexing to print the last item in your first_list
print(first_list[-1])

# 7. Create a new list with 7 items and use a range of indexes 
# to print the 3rd, 4th and 5th items.
another_list = [1, 2, 3, 4, 5, 6, 7]
for item in range(0, 7):
    print(another_list[2], another_list[3], another_list[4])

# 8. Write a list of countries and make a copy of it.
countries_list = ["Uganda", "Kenya", "Tanzania"]
copy_of_countries_list = countries_list.copy()
print(copy_of_countries_list)

# 9. Write a python program to loop through the list of countries
for country in countries_list:
    print(country)

# 10. Write a list of animal names 
# and sort them in both descending and ascending order.
animal_names = ["Dog", "Cat", "Horse"]
animal_names.sort()
print(f"Ascending: {animal_names}")
animal_names.sort(reverse = True)
print(f"Descending: {animal_names}")

# 11. Using the list above, write a python program 
# to output only animal names with the letter
# ‘a’ in them
for animal in animal_names:
    if animal.__contains__("a"):
        print(animal)

# 12. Write two lists, one containing your 
# first names and the other your second names. Join the two lists.
first_names = ["John", "Sam", "Mary"]
second_names = ["Ssebuliba", "Angoda", "Lutalo"]

first_names.extend(second_names)
print(first_names)

# TUPLES

# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("Samsung", "iPhone", "tecno", "redmi")
fav_phone_brand = x[0]
print(fav_phone_brand)

# 2. Use negative indexing to print the 2nd last item in your tuple.
second_last_item = x[-2]
print(second_last_item)

# 3. Using the phones list above, 
# write a python program to update “iphone” to “itel”
convert_x = list(x)
convert_x[1] = "itel"
tupled = tuple(convert_x)
print(tupled)

# 4. Write a python program to add “Huawei” to your tuple.
add_huawei = list(x)
add_huawei.append("Huawei")
tupled_2 = tuple(add_huawei)
print(tupled_2)

# 5. Write a python program to loop through the tuple above.
for item in tupled_2:
    print(item)

# 6. Write a python program to remove/delete 
# the first item in your tuple.
remove_first_item = list(tupled_2)
remove_first_item.pop(0) # Removes Samsung
tupled_3 = tuple(remove_first_item)
print(tupled_3)

# 7. Using the tuple() constructor, 
# create a tuple of the cities in Uganda.
cities_in_uganda = tuple(("Kampala", "Masaka", "Mukono", "Jinja"))
print(cities_in_uganda)
print(type(cities_in_uganda))

# 8. Write a python program to unpack your tuple.
for city in cities_in_uganda:
    print(city)

# 9. Use a range of indexes to print 
# the 2nd, 3rd and 4th cities in your tuple above.
print(cities_in_uganda[1:4])

# 10.  Write two tuples, one containing your 
# first names and the other your second names. Join the two tuples.
first_names = ("Wilfred", "John", "Sara", "Mercy")
sur_names = ("Angoda", "Lutalo", "Muhumuza", "Kira")
full_name = first_names + sur_names
print(full_name)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("Red", "Orange", "Yellow")
multiple_colors = colors * 3
print(multiple_colors)
print(type(multiple_colors))

# 12. Return the number of times 8 appears in this tuple
    #   thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
counter = 0
for number in thistuple:
    if number == 8:
        counter = counter + 1
print(counter)

# SETS

# 1. Use the set() constructor 
# to create a set of 3 of your favorite beverages.
beverages = set({
    "Smirnoff", "Nile Special", "Almeca"
})
print(beverages)
print(type(beverages))

# 2. Use the correct method to add 2 more items to the beverages set.
beverages.add("Club")
beverages.add("Jameson")
print(beverages)

# 3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

check_item = "microwave"
# Un comment to use user input
# check_item = str(input("Enter the item to check: ").lower())

if check_item in mySet:
    print(f"The item {check_item} exists")
else:
    print(f"The item {check_item} doesn't exist")

# 4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet)

# 5. Write a python program to loop through the set above.
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. 
# Write a python program to add elements in
# the list to elements in the set.
set_of_4 = {"One", "Two", "three", "four"}
list_of_two = [1, 2]

union_collection = set_of_4.union(list_of_two)
print(union_collection)
# ALSO
set_of_4.update(list_of_two)
print(set_of_4)

# 7. Write two sets, one containing your ages 
# and the other your first names. Join the two sets.
first_set = {29, 21, 22}
first_names = {"Angoda", "John", "Susan"}

new_set = first_set.union(first_names)
print(new_set)

# STRINGS

# 1. Declare two variables, an integer and a string 
# and use the correct method to concatenate the two variables.
age = 29
name = "Angoda"

bio = str(age) + " " + name
print(bio)
# ALSO
print(f"{age} {name}")

# 2. Consider the example below;
# txt = “ Hello, Uganda! ”
# Output the string without spaces at the beginning, 
# in the middle and at the end.

txt = " Hello, Uganda! "
stripped = txt.strip()
print(stripped)

# 3. Write a python program to 
# convert the value of ‘txt’ to uppercase.
capitalize = stripped.upper()
print(capitalize)

# 4. Write a python program to replace character 
# ‘U’ with ‘V’ in the string above.
replaced = stripped.replace("U", "V")
print(replaced)

# 5. Using the code below, write a python program 
# to return a range of characters in the 2nd,
# 3rd and 4th position.
# y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
print(y[1:4])

# 6. The piece of code below will give an error when output; 
# x = “All “Data Scientists” are cool!”
# Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)


# DICTIONARIES 

# 1. With reference to the dictionary below, 
# write a python program to print the value of the shoe size.
shoes = {
    "brand" : "Nick",
    "color" : "black", 
    "size" : 40
}
print(f"the value of shoes is {len(shoes)}")

# 2. Write a python program to change the value “Nick” to “Adidas”
shoes["brand"] = "Adidas"
print(shoes)

# 3. Write a python program to add a key/value pair 
# "type”: "sneakers" to the dictionary
shoes.update({
    "type": "sneakers"
})

print(shoes)

# 4. Write a python program to return a 
# list of all the keys in the dictionary above.
list_of_all_keys = shoes.keys()
print(list_of_all_keys)

# 5. Write a python program to return a 
# list of all the values in the dictionary above.
list_of_all_values = shoes.values()
print(list_of_all_values)

# 6. Check if the key “size” exists in the dictionary above.
for key in shoes.keys():
    if key == "size":
        print(f"{key} exists")

# 7. Write a python program to loop through the dictionary above.
for item in shoes:
    print(item)

# 8. Write a python program to remove “color” from the dictionary.
shoes.pop("color")
print(shoes) 

# 9. Write a python program to empty the dictionary above.
shoes.clear()
print(f"shoes size is {len(shoes)}")

# 10. Write a dictionary of your choice and make a copy of it.
dictionary = {
    "name": "Angoda Brian Nyanga",
    "age": 29
}

dictionary_copy = dictionary.copy()
print(dictionary_copy)

# 11. Write a python program to show nested dictionaries
nested_dictionary = {
    "original": {
        "name": "Angoda Brian Nyanga",
        "age": 29
    },
    "another": {
        "me": "You",
        "him": "her"
    }
}

print(nested_dictionary)