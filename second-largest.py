arr = [10,52,5,14,8,25,74,15,65,11]

largest = float("-inf")

second_largest = float("-inf")

if len(arr) < 2:

    print("Second largest element does not exist.")

else:

    for num in arr:

        if num > largest:

            second_largest = largest

            largest = num

        elif num > second_largest and num != largest:

            second_largest = num

    print("largest element is:", largest)

    if second_largest == float("-inf"):

        print("Second largest element does not exist.")

    else:

        print("second largest element is:", second_largest)