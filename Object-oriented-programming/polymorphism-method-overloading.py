class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()

print(c.add(5, 10))
print(c.add(5, 10, 15))
print(c.add(5, 10, 15, 20))
print(c.add(5, 10, 15, 20, 25))