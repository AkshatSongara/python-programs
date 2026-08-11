def array_length(array):

    count = 0

    for element in array:

        count = count + 1

    return count

array = [10,20,30,40,50]

result = array_length(array)

print("Length of array is: ", result)