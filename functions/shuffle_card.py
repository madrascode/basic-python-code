import itertools, random
def shuffle_card():
    deck = list(itertools.product(range(1, 14), ['Spade', "Heart", "Diamond", "Club"]))
    random.shuffle(deck)

    for i in range(5):
        print(deck[i][0], "of", deck[i][1]) # here deck[i][0] -- 5 denotes to number and deck[i][1] denotes to card name -- Club

print(shuffle_card())
