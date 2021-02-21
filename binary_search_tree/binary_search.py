# binary search using two different functions. 

def locate_cards(list_of_card, target):
    def condition(mid):
        if list_of_card[mid] == target:
            if mid - 1 >= 0 and list_of_card[mid - 1] == target:
                return 'left'
            else:
                return 'found'
        elif list_of_card[mid] < target:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(list_of_card)-1, condition)        

def binary_search(lo,hi,condition):
    # lo = 0
    # hi = len(list_of_cards)-1
    while lo <= hi :
        mid = (lo + hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1



 # binary search using single function. 
def binary_search(list_of_card, target):
    lo = 0
    hi = len(list_of_card)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        print('lo:',lo,'hi:',hi, 'mid:', mid, 'mid_element:', list_of_card[mid])
        
        if list_of_card[mid] == target:
            if mid - 1 >= 0 and list_of_card[mid-1]==target: # if there are more than one occurence of target value then we have to move towards left value
                hi = mid - 1    
            else:
                return mid 
        elif list_of_card[mid] < target:
            hi = mid - 1 # for left side
        else:
            lo = mid + 1
    return -1

print(binary_search([3,3,3,3,3,2,2,2,2,2,1], 3))