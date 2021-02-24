'''You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].'''

def linear_rotated_search(list_of_num):

    count = 0
    while count < len(list_of_num):
        print(count)
        if count > 0 and list_of_num[count-1]>list_of_num[count]: # count>0 is applied for 0th element becase there exist no element before 0th element
            print(count)
            return count
        else:
            count += 1
    return 0

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return 0


def binary_rotated_array(list_of_num):
    lo = 0
    hi = len(list_of_num)-1
    def condition(mid):
        # position = 0
        if mid > 0 and list_of_num[mid - 1] > list_of_num[mid]:
            return 'found'
        elif list_of_num[mid] < list_of_num[hi]:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(list_of_num)-1, condition) 

def target_array_value(list_of_num, target):
    pivot = binary_rotated_array(list_of_num)
    def condition(mid):
        if list_of_num[mid] == target:
            return 'found'
        if list_of_num[pivot] < list_of_num[len(list_of_num)-1]:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(list_of_num)-1, condition)
    

# print(linear_rotated_search([3,1,0]))
# print(binary_rotated_array([5,1,2,3,4]))
print(target_array_value([1,2,3,4,5,6,7,8,9], 4))