def array_sum(array):

    total = 0

    for num in array:

        total = total + num

    return total

array = [1,2,3,4,5]

result = array_sum(array)

print("Sum of array element is:", result)