import sys
from collections import Counter 

def identify_hand(hand):
    frecuencies = Counter(hand)

    pairs = [value for value, frecuency in frecuencies.items() if frecuency == 2]
    threes = [value for value, frecuency in frecuencies.items() if frecuency == 3]
    fours = [value for value, frecuency in frecuencies.items() if frecuency == 4]
    fives = [value for value, frecuency in frecuencies.items() if frecuency == 5]

    jokers = hand.count('J')

    if fives:
        strength = "five"
    elif fours:
        strength = "four"
    elif len(threes) == 1 and len(pairs) == 1:
        strength = "full"
    elif len(threes) == 1:
        strength = "three"
    elif len(pairs) == 2:
        strength = "double-pair"
    elif len(pairs) == 1:
        strength = "pair"
    else:
        strength = "high"

    if strength == "four" and jokers != 0:
        return "five"
    elif strength == "full" and jokers != 0:
        return "five"
    elif strength == "three" and (jokers == 1 or jokers == 3) or strength == "double-pair" and jokers == 2:
        return "four"
    elif strength == "double-pair" and jokers == 1:
        return "full"
    elif strength == "pair" and jokers != 0:
        return "three"
    elif strength == "high" and jokers == 1:
        return "pair"
    else:
        return strength


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
    scores[strength] = sorted(scores[strength] + [hand], key=lambda x: tuple('J23456789TQKA'.index(c) for c in x[0]))

multiplier = 1
for strength in scores.values():
    for hand in strength:
        score += int(hand[1])*multiplier
        multiplier += 1
print(score)