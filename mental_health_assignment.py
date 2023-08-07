# Author: Angoda Brian Nyanga
# Session: Morning

# CONDITIONAL LOGIC

# if else
print("#" * 50)
print("# 1. Conditional logic with if else.")
print("#" * 50)
age = 17

if age > 18 or age == 18:
    print('adult')
elif age <= 12:
    print('kid')
else:
    print('teenager')

# Dictionaries
# 1. key-value. 2. key is unique. 3. key is immutable. 
# 4. value is mutable. 5. value can be duplicated. Ordered
print("\n")
print("#" * 50)
print("# 2. Dictionaries.")
print("#" * 50)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print(d.get('Michael')) # Another way to get value from dict. But it has a default value of None
print(d.get('Me', -1)) # -1 is default value. Useful when key is not in dict
print(len(d))


# Loops. DO & WHILE
# for loop
names = ['Michael', 'Bob', 'Tracy', 'Bob']
print("\n")
print("#" * 50)
print("# 3. The for loop.")
print("#" * 50)
for name in names:
    print(name)

print("\n")
print("#" * 50)
print("# 4. The while loop.")
print("#" * 50)
i = len(names) - 1
while i >= 0:
    print(names[i])
    i -= 1

# CONTINUE & BREAK STATEMENTS
names = ['Michael', 'Bob', 'Tracy', 'Bob']
print("\n")
print("#" * 50)
print("# 5. Using break and continue statements.")
print("#" * 50)

for name in names:
    # if name == 'Bob':
    #     print(name)
    #     continue
    
    if name == 'Bob':
        print(name)
        break
    
# EXCEPTION HANDLING USING TRY & EXCEPT
numbers = [1, 2, 3]
print("\n")
print("#" * 50)
print("# 6. Exception Handling using try & except.")
print("#" * 50)

try:
    print(numbers[5])
except IndexError as error:
    print("IndexError: ", error)
finally:
    print("This will always execute")

print("\n")
print("#" * 50)
print("# 7. Exercise.")
print("#" * 50)
""" 
    EXERCISE ON EXCEPTION HANDLING, DICTIONARIES, LOOPS, AND CONTROL FLOW
    Prompt students on a scale of 1 - 10, to rate their mental health
"""

emotion = {
    1: 'Too bad.',
    2: 'Take a walk.',
    3: 'Remember the movie Joy.',
    4: 'Sorrow is a valid emotion.',
    5: 'Not too bad.',
    6: 'Take a deep breath.',
    7: 'You are loved.',
    8: '8 is good. 8 is great.',
    9: 'You are strong.',
    10: 'You are beautiful.',
}

emote = ''
CRED = '\033[91m'
CEND = '\033[0m'
SUCCESS = '\033[92m'


while(emote != 'q'):
    emote = input("On a scale of 1 - 10, how are you feeling today? Enter 'q' to quit. ")

    try:
        if emote == 'q':
            print(SUCCESS + "Goodbye. Have a great day!" + CEND)
            print("\n")
            break
        else:
            emote = int(emote)
    except ValueError:
        if emote == '':
            print(CRED + "You didn't enter anything." + CEND)
        else:
            print(CRED + f"You entered '{emote}'. Please enter a number between 1 - 10." + CEND)
        print("\n")
        continue

    if emote in emotion:
        print(SUCCESS + emotion[emote] + CEND)
        print(SUCCESS + "Thank you for rating your mental health." + CEND)
        print("\n")
    else:
        print(CRED + "I don't recognize that rating." + CEND)
        print("\n")








