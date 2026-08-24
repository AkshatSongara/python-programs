class Car:

    model = ""

    color = ""

    price = 0


    def show(self):

        print("Car model:", self.model)
        print("Car color:", self.color)
        print("Car price:", self.price)


c1 = Car()
c2 = Car()

c1.model = "Mercedes"
c1.color = "grey"
c1.price = 1500000

c1.show()

c2.model = "Audy"
c2.color = "White"
c2.price = 5000000

c2.show()