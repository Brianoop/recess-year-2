# if else
age = 17

# if age > 18 or age == 18:
#     print('adult')
# elif age <= 12:
#     print('kid')
# else:
#     print('teenager')

# Dictionaries
# 1. key-value. 2. key is unique. 3. key is immutable. 
# 4. value is mutable. 5. value can be duplicated. Ordered
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
# print(d.get('Michael'))
# print(d.get('Me', -1)) # -1 is default value. Useful when key is not in dict
# print(len(d))


# Loops. DO & WHILE
# for loop
names = ['Michael', 'Bob', 'Tracy', 'Bob']
# for name in names:
#     print(name)

# i = len(names) - 1
# while i >= 0:
#     print(names[i])
#     i -= 1

# CONTINUE & BREAK STATEMENTS
names = ['Michael', 'Bob', 'Tracy', 'Bob']

for name in names:
    # if name == 'Bob':
    #     print(name)
    #     continue
    
    if name == 'Bob':
        print(name)
        break
    