from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car start with key")

    def stop(self):
        print("Car stops with break")

class Bike(Vehicle):

    def start(self):
        print("Bike start with self-start")

    def stop(self):
        print("Bike stops with break")

car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()