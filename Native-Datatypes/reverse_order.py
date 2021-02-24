# reverse string 
# element count in an array
# reverse order of string in a string

def len_count(string):
    count = 0
    for _ in string:
        count += 1
    return count


def rev_order(string):
    return string[len_count(string)::-1]

def rev_word_order(string):
    string_revered = rev_order(string)
    print(string_revered)
    tmp = ''
    reversed_string = ''
    for c in string_revered:
        if c != ' ':
            tmp += c
            # print(tmp)
        else:
            reversed_string += (rev_order(tmp)) + " "
            # print(tmp)
            tmp = ''
    if tmp:
        reversed_string += (rev_order(tmp))
    return (reversed_string)

print(rev_word_order("you shall not pass"))
    

def count_array_element(arr):
    dict = {}
    i = 0
    while i < len(arr):
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] += 1
        i += 1
    return dict

print(count_array_element([10,15,14,14,1,10,10]))

