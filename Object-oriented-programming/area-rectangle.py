class Reactangle:

    length = 0
    width = 0

    def area(self):

        return self.length * self.width

    def perimeter(self):

        return 2 * (self.length + self.width)


r1 = Reactangle()
r2 = Reactangle()

r1.length = 15
r1.width = 20

print("Area of reactangle:", r1.area())
print("Area of perimeter:", r1.perimeter())

r2.length = 25
r2.width = 5

print("Area of reactangle:", r2.area())
print("Area of perimeter:", r2.perimeter())