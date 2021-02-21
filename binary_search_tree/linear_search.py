# linear search program using for loops
def traverse_cards(list_of_cards, target):
    for i in range(len(list_of_cards)):
        # print(list_of_cards[i])
        if list_of_cards[i] == target:
            return i
    else:
        return -1

# linear search program using while loops
def locate_cards(list_of_cards, target):
    position = 0
    while position < len(list_of_cards):
        # print("position",position)
        if list_of_cards[position] == target:
            if list_of_cards[position + 1] == target: # this condition is for our target value repeating  more than one time in a list. 
                position = position + 1
                return position
            return position - 1
        position += 1
        # if position == len(list_of_cards):
        #     return -1
    return -1
    
result = traverse_cards([3, 2, 2, -1, -2], 2)
result_while = locate_cards([3, 2, 2, 2, -1], 2)
print(result_while)
print(result)