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

print(linear_rotated_search([3,1,0]))
