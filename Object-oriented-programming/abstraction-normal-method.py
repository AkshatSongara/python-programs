from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

dog = Dog()

dog.eat()
dog.sound()