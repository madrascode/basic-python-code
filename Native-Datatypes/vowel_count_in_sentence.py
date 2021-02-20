def count_vowel(sentence):

    vowels = '''aeiou'''
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

sentence = 'Hello have you tried our tutorial section'

print(count_vowel(sentence))

def dict_vowel_count(sentence):
    vowels = 'aeiou'
    count_dict = {}.fromkeys(vowels, 0)

    sentence = sentence.casefold()
    for char in sentence:
        if char  in count_dict:
            count_dict[char] += 1
    print(count_dict)

dict_vowel_count("Hello have you tried our tutorial section")
