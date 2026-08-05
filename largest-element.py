lst = [5, 15, 25, 7, 14, 35, 23, 20, 55, 31]

if len(lst) == 0:

    print("The list is empty. No largest element.")

else:

    largest = lst[0]

    for num in lst:

        if largest < num:

            largest = num

    print("Largest Number is : ", largest)