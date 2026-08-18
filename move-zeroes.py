def moves_zeroes(nums):

    write = 0

    for read in range(len(nums)):

        if nums[read] != 0:

            temp = nums[write]

            nums[write] = nums[read]

            nums[read] = temp

            write = write + 1

    return nums

nums = [0,1,0,3,12]

result = moves_zeroes(nums)

print(nums)