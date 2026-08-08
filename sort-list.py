def Bubble_sort(lst):

    n = len(lst)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if lst[j] > lst[j + 1]:

                temp = lst[j]

                lst[j] = lst[j + 1]

                lst[j + 1] = temp

    return lst

lst = [20, 10, 30, 15, 35, 5, 60, 50, 55, 90]

print("List before Sorting : ", lst)

result = Bubble_sort(lst)

print("List after sorting : ", result)