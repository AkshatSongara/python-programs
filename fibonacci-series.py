number = int(input("Enter a Number : "))

prev = 1

nxt = 0

curr = 0

for i in range(1, number + 1):

    print(curr, end = " ")

    curr = prev + nxt

    prev = nxt

    nxt = curr