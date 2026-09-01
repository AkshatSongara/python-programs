class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

class Cat(Animal):
    def sound(self):
        print("Meow")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()