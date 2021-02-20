def len_of_string(word):
    count = 0
    for _ in word:  # here _ is throwaway variable...because we dont want it to be used to store any value
        count += 1
    return count # this function gives output of 7...like len() function of python. 


def check_palindrome(word):
    lo = 0
    hi = len_of_string(word)-1
    word = word.casefold()  # will convert all letters to lower case
    print(word)
    while lo <= hi:
        if word[lo] != word[hi]:
            print(word[lo],"and", word[hi], "are not matching!")
            # print(word[hi])
            return False
        lo += 1
        hi -= 1
        
    return True

print(check_palindrome(' aBcdCbA ')) 