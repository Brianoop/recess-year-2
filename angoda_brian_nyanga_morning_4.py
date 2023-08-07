# OOP in Python
# Classes
    # When you define a class in Python, every method 
    # that you define, must accept that instance as 
    # its first argument (called self by convention)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def start_engine(self):
        print("Engine started")


    def stope_engine(self):
        print("Stop Engine")


# create instance of car
my_car = Car("Toyota", "Corona", 2007)
# my_car.start_engine()


class Bank:
    # Define the constructor
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    

    # Define the methods
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    

    def check_balance(self):
        return self.balance


# Create an instance of the Bank class
my_account = Bank("BRIAN", "123456789", 1000)
# print(my_account.check_balance())
# print(my_account.deposit(500))
# print(my_account.withdraw(200))
# print(my_account.check_balance())


class Human:
    # create a constructor
    # self is a reference to the current instance of the class
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # create methods
    def eat(self, name):
        print(f"{self.name} is eating")


    def sleep(self, color):
        print(f"A {self.color} man sleeping")


    def walk(self, age, name):
        print(f"At age {self.age}, {self.name} is still walking")


# create instance of Human
majaliwa = Human("Majaliwa", 29, "Black")
# majaliwa.eat("Majaliwa")
# majaliwa.sleep("Black")
# majaliwa.walk(29, "Majaliwa")


class Circle:
    # create a constructor
    def __init__(self, radius):
        self.radius = radius


    # create methods
    def area(self):
        return 3.14 * self.radius * self.radius


    def perimeter(self):
        return 2 * 3.14 * self.radius
    

circle = Circle(7)
# print(circle.radius)
# Area
# print(circle.area())
# Perimeter
# print(circle.perimeter())


class Rectangle:
    # create a constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width


    # create methods
    def area(self):
        return self.length * self.width


    def perimeter(self):
        return 2 * (self.length + self.width)
    

rectangle = Rectangle(10, 5)
# print(rectangle.length)
# print(rectangle.width)
# Area
# print(rectangle.area())
# Perimeter
# print(rectangle.perimeter())


class Employee:
    # create constructor
    def __init__(self, name, salary, bonus = 0.15):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    # create display method
    def display_bonus(self):
        print(f"Employee name: {self.name}")
        # calculate bonus
        bonus = self.bonus * self.salary
        print(f"{self.name}'s bonus is: {bonus:.0f}")


employee1 = Employee("BRIAN", 150000)
# employee1.display_bonus()

employee2 = Employee("Majaliwa", 230000)
# employee2.display_bonus()


# Encapulsation

# Encapsulation is the process of restricting access 
# to methods and variables in a class in order 
# to prevent direct data modification so 
# it prevents accidental modification of data

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private variable. age is encapsulated


    def display_age(self):
        print(f"{self.name} is {self.__age} years old")


    # create getter method for age
    def get_age(self):
        return self.__age


person = Person("BRIAN", 29)
name = person.name
# print(person.name)
# print(person.__age) # this will throw an error
name = "Majaliwa"
person.age = 30 # age is private. This will not work
# print(name)
# print(person.get_age())


class Temperature:
    def __init__(self, temperature):
        # self._temperature = temperature # this is not encapsulated
        self.__temperature = temperature # this is encapsulated


    # get temperature
    def get_temperature(self):
        return f"{self.__temperature:.2f}"

    def to_fahrenheit(self):
        return (self.__temperature * 1.8) + 32


    def to_celsius(self):
        return (self.__temperature - 32) * 5/9
    

temperature = Temperature(37)
# temperature.__temperature = 100 # change temperature to 100 won't work
# print(temperature.__temperature)
fahrenheit = temperature.to_fahrenheit()
# print(f"{temperature.get_temperature()}C = {fahrenheit:.2f}F")

# # Assignment 1:  Show encapsulation with employee information 
# to give a pay increamentation 
# (Salary with employee information to new_salary)e.g 
# from 850000 to 1000000

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    
    def display_salary(self):
        print(f"{self.name}'s salary is {self.__salary}")
    

    # Increase salary
    def increase_salary(self, new_salary):
        self.__salary = new_salary
        print(f"{self.name}'s new salary is {self.__salary}")

    
employee = Employee("BRIAN", 850000)
employee.display_salary() # prints salary = 850000
employee.increase_salary(1000000)
employee.__salary = 5000000 # this will not work because salary is encapsulated. it's restricted and can't be modified from outside the class
employee.display_salary() # prints new_salary = 1000000



        