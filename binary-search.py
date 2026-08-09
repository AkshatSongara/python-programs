def binary_search(arr, size, target):

    start = 0

    end = size - 1

    while(start <= end):

        mid = start + (end - start) // 2

        if arr[mid] == target:

            return mid

        elif arr[mid] > target:

            end = mid - 1

        else:

            start = mid + 1

    return -1


arr = [2, 5, 6, 8, 10, 15, 55]

target = int(input("Enter the target value : "))

size = len(arr)

index = binary_search(arr, size, target)

if index == -1:

    print("Search result: Target value not found.")

else:

    print("Target value :", target)

    print("Index value :", index)