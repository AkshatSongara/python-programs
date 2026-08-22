list1 = [1,2,3,4,5]

list2 = [4,5,6,7,8]

common = []

count = 0

for i in range(len(list1)):

    for j in range(len(list2)):

        if list1[i] == list2[j]:

            common = common + [list1[i]]

            count = count + 1

            break

print("Common Elements:", common)

print("Common Elements Count:", count)