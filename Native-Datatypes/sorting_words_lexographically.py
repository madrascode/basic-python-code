def sort_em_all(sentence):
    list_of_words = sentence.split()
    list_of_words.sort()

    return list_of_words
    
sentence = 'Hello this Is an Example sentence With cAsed LettErS.'

result = sort_em_all(sentence)

for i in result:
    print(i, end=" ")