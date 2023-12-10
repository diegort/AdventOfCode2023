import sys
from collections import Counter 

def identify_hand(hand):
    frecuencies = Counter(hand)

    pairs = [value for value, frecuency in frecuencies.items() if frecuency == 2]
    threes = [value for value, frecuency in frecuencies.items() if frecuency == 3]
    fours = [value for value, frecuency in frecuencies.items() if frecuency == 4]
    fives = [value for value, frecuency in frecuencies.items() if frecuency == 5]

    #valores_ordenados = sorted(set(hand), key=lambda x: '23456789TJQKA'.index(x))

    if fives:
        return "five"
    elif fours:
        return "four"
    elif len(threes) == 1 and len(pairs) == 1:
        return "full"
    elif len(threes) == 1:
        return "three"
    elif len(pairs) == 2:
        return "double-pair"
    elif len(pairs) == 1:
        return "pair"
    else:
        return "high"


D = open(sys.argv[1]).read().strip().splitlines()
score = 0
game = [tuple(line.split()) for line in D]

scores = {
    "high": [],
    "pair": [],
    "double-pair": [],
    "three": [],
    "full" : [],
    "four" : [],
    "five" : []
}

for index, hand in enumerate(game):
    cards = hand[0]
    strength = identify_hand(cards)
    scores[strength] = sorted(scores[strength] + [hand], key=lambda x: tuple('23456789TJQKA'.index(c) for c in x[0]))

multiplier = 1
for strength in scores.values():
    for hand in strength:
        score += int(hand[1])*multiplier
        multiplier += 1
print(score)