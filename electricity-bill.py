units = int(input("Enter electricity units: "))

if units < 0:

    print("Invalid units.")


elif units <= 100:

    bill = units * 1.50

    print("Electricity Bill = ", bill)


elif units <= 200:

    bill = (100 * 1.50) + ((units - 100) * 2.50)

    print("Electricity Bill = ", bill)


elif units <= 300:

    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4)

    print("Electricity Bill = ", bill)


else:

    bill = (100 * 1.50) + (100 * 2.50) + (100 * 4) + ((units - 300) * 5)

    print("Electricity Bill = ", bill)