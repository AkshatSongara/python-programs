def remove_duplicates(arr):

    if len(arr) == 0:

        return 0

    i = 0

    for j in range(1, len(arr)):

        if arr[i] != arr[j]:

            i = i + 1

            arr[i] = arr[j]

    return i + 1


arr = [1,1,2,2,3]

n = remove_duplicates(arr)

print("After removing duplicates : ", arr[:n])