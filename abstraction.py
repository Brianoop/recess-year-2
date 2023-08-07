# Abstraction in Python

from abc import ABC, abstractmethod

# You can inherit from ABCMeta and use metaclass
# from abc import ABCMeta, abstractmethod
# class Parent(metaclass = ABCMeta):
#     pass

# class Animal(Parent):
#     @abstractmethod
#     def breathe(self):
#         pass

class Animal(ABC):
    @abstractmethod
    def breathe(self):
        pass


class Dog(Animal):
    def breathe(self):
        print("I breathe")


def main():
    rose = Dog()
    rose.breathe()
    
if __name__ == "__main__":
    main()
