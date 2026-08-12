def count_even(arr):

    count = 0

    for num in arr:

        if num % 2 == 0:

            count = count + 1

    return count


def count_odd(arr):

    count = 0

    for num in arr:

        if num % 2 != 0:

            count = count + 1

    return count


arr = [1,2,3,4,5,6,7,8,9,10,12]

result_even_count = count_even(arr)

result_odd_count = count_odd(arr)

print("Even count:", result_even_count)

print("Odd count:", result_odd_count)