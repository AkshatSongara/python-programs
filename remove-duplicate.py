array = [5,10,20,10,5,25,50,25,100]

unique = []

for num in array:

    found = False

    for item in unique:

        if num == item:

            found = True

            break

    if found == False:

        unique.append(num)


print("Original array:", array)

print("Array after removing duplicates:", unique)