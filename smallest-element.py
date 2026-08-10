def find_smallest(arr):

    if len(arr) == 0:

        return None
    

    smallest = arr[0]

    for num in arr:

        if num < smallest:

            smallest = num

    return smallest


arr = [25, 15, 30, 7, 14, 35, 23, 20, 55, 31]

result = find_smallest(arr)


if result is None:

    print("The array is empty. No smallest element.")

else:

    print("Smallest number in array is :", result)