from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
cardStrength = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
}

@dataclass
class hand:
    type: int = 1
    cards: str = ''
    bid: int = 0

def typeCombinations(threes, twos):
    if (threes and twos):
        return 5
    elif (threes):
        return 4
    elif (twos == 2):
        return 3
    elif (twos):
        return 2
    return 1

def getCardType(cards, bid):
    h = hand()
    uniqueCards = set()
    threes = 0
    twos = 0
    for card in range(len(cards)):
        uniqueCards.add(cards[card])
    for card in uniqueCards:
        cardOccur = cards.count(card)
        if (cardOccur == 5):
            h.type = 7
        elif cardOccur == 4:
            h.type = 6
        elif cardOccur == 3:
            threes += 1
        elif cardOccur == 2:
            twos += 1
    if (threes or twos):
        h.type = typeCombinations(threes, twos)
        
    h.cards = cards
    h.bid = bid
    return h

def weakerHand(p1, p2):
    for i in range(len(p1)):
        if (p1[i] != p2[i]):
            return cardStrength[p1[i]] <= cardStrength[p2[i]]
    return False

# https://www.educative.io/answers/how-to-implement-quicksort-in-python 
def sortHands(hand):
    elements = len(hand)
    #Base case
    if elements < 2:
        return hand
    current_position = 0 #Position of the partitioning element
    for i in range(1, elements): #Partitioning loop
        if hand[i].type < hand[0].type or (hand[i].type == hand[0].type and weakerHand(hand[i].cards, hand[0].cards)):
            current_position += 1
            temp = hand[i]
            hand[i] = hand[current_position]
            hand[current_position] = temp
    temp = hand[0]
    hand[0] = hand[current_position] 
    hand[current_position] = temp #Brings pivot to it's appropriate position
    left = sortHands(hand[0:current_position]) #Sorts the elements to the left of pivot
    right = sortHands(hand[current_position+1:elements]) #sorts the elements to the right of pivot
    hand = left + [hand[current_position]] + right #Merging everything together
    return hand

hands = []
for line in lines:
    handInfo = line.split(' ')
    hands.append(getCardType(handInfo[0], int(handInfo[1])))


hands = sortHands(hands)
sum = 0
for i in range(len(hands)):
    sum += hands[i].bid * (i+1)

print(sum)