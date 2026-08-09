def linear_search(arr, size, target):

    for i in range(size):

        if arr[i] == target:

            return i

    return -1


arr = [1,2,3,4,5]

target = int(input("Enter the Target value : "))

size = len(arr)

index = linear_search(arr, size, target)

if index == -1:

    print("target value not found.")

else:

    print("Target Value :", target)

    print("Target index :", index)