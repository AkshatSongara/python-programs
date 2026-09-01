class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog:
    def speak(self):
        print("Dog Barks")

class Cat:
    def speak(self):
        print("Cat Meow")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.speak()