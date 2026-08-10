def find_missing(arr, n):

    if len(arr) == 0:

        return None

    expected_sum = n * (n + 1) // 2

    actual_sum = sum(arr)

    missing_number = expected_sum - actual_sum

    return missing_number

arr = [1,3,4,5]

n = 5

result = find_missing(arr, n)

print("Missing number in array is : ", result)