import re 

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# Needed for Part 2
cards = {}
for cardNmbr in range(1, len(lines)+1):
    cards[cardNmbr] = 1

# Part 1 & Part 2
sum = 0
for cardNmbr in range(len(lines)):
    count = 0 # For point system that doubles 
    matchings = 0 # Used to get the scratchcards below a card number
    cardInfo = lines[cardNmbr].split('|')
    winnings = re.findall('\d+', cardInfo[0].split(':')[1]) # split is necessary for not counting the card number
    numbers = re.findall('\d+', cardInfo[1])
    for number in numbers:
        if number in winnings:
            count = 1 if count == 0 else count * 2
            # Part 2 
            matchings += 1 
            scoreCard = (cardNmbr + 1) + matchings
            # The number of copies of a certain card will impact the amount of cards won 
            copies = cards[cardNmbr + 1] 
            cards[scoreCard] = cards.get(scoreCard) + copies
    sum += count

print(sum)

# Gets total scratchcards
sum = 0
for card, copies in cards.items():
    sum += copies
print(sum)