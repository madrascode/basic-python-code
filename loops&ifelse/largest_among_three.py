def largest_num(nums):
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest

large = largest_num([4,3,5,2,6,1,7])

print(large)