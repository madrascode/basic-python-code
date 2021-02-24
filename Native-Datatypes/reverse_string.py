def len_str(string):
    count = 0
    for _ in string:
        count += 1
    return count

def string_reversed(string):
    len_string = len_str(string)-1
    # print(len_string)
    string_reversed = ''
    dict_count = {}

    while len_string >= 0:
        string_reversed += string[len_string]
        
        if string[len_string] not in dict_count:
            dict_count[string[len_string]] = 1
        else:
            dict_count[string[len_string]] += 1

        len_string -= 1
    return string_reversed # , dict_count

# print(string_reversed('Hello World!'))

def string_splitter(string):
    tmp = ''
    splitted_list = []
    for c in string:
        if c != ' ':
            tmp += c
        else:
            splitted_list += tmp[::-1]
            tmp = ''
    if tmp:
        splitted_list += tmp[::-1]
        
    return ''.join(splitted_list)

print(string_splitter("Hello World")) 