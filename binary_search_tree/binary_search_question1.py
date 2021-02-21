'''Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.'''
# numbers in the list are sorted in ascending order. [1,2,3,4,4,4,4,4,4,5,6,7,8,9,10]
# we have to find the starting and ending position of a given number. start_position = 3 and end_position = 8

# generic binary search

def binary_search(lo, hi ,condition):
    print(lo+hi//2, hi)
    while lo <= hi:        
        mid = (lo+hi) // 2
        result  = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo  = mid + 1
    return -1


def first_occurence(list_of_numbers, target):
    def condition(mid):
        if list_of_numbers[mid]== target:
            if mid - 1 >= 0 and list_of_numbers[mid-1]==target:
                return 'left'
            else:
                return 'found'
        elif list_of_numbers[mid]>target:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(list_of_numbers)-1, condition)

def last_occurence(list_of_numbers, target):
    def condition(mid):
        # print(mid,len(list_of_numbers)-1)
        if list_of_numbers[mid]==target:
            if mid < len(list_of_numbers)-1  and list_of_numbers[mid + 1] == target: # we are applying this condition mid < len(list_of_numbers)-1 ... so that only one value will be left on the right side and we can check that using mid + 1 == target condition. 
                print(mid, len(list_of_numbers)-1)
                return 'right'
            else:
                return 'found'
        elif list_of_numbers[mid] > target:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(list_of_numbers)-1, condition)

# print(first_occurence([2], 2)) # 1
print(last_occurence([], 2)) # 5
