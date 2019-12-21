import random


#  Game dynamics (betting system)
#  Decide the Winner Globally

# Before coding any algorithm, it is necessary to do the pseudocode or the flowchart of each one
# • It is necessary to do a flowchart indicating the global interaction among all the functions

# Dealer’s and user’s cards
# Deliveries: (100%)
# o Tests scenario to validate functionality of each algorithm and different possible cases (10%)
# o Pseudocodes or flowcharts of each algorithm to code in pdf (10%)
# o Flowchart of the global interaction among all the functions in pdf (5%)
# o Python code of each algorithm in a python file (40%)
# o Python code of the global interaction in a python file (10%)
# o Python code with Execution and validation of each test scenario (25%)
# o Total files to deliver: 6


def createdeck():
    '''Create a new deck of cards, (which is a dictionary) from three different arrays, each with a different specification.'''
    cards = ["🂢", "🂣", "🂤", "🂥", "🂦", "🂧", "🂨", "🂩", "🂪", "🂫", "🂭", "🂮", "🂡", "🂲", "🂳", "🂴", "🂵", "🂶",
             "🂷", "🂸", "🂹", "🂺", "🂻", "🂽", "🂾", "🂱", "🃂", "🃃", "🃄", "🃅", "🃆", "🃇", "🃈", "🃉", "🃊", "🃋",
             "🃍", "🃎", "🃁", "🃒", "🃓", "🃔", "🃕", "🃖", "🃗", "🃘", "🃙", "🃚", "🃛", "🃝", "🃞", "🃑"]
    dictCards = []
    suits = ["♠", "♥", "♦", "♣"]
    suitchange = 0
    value = 0
    for i in range(0, 52):
        if i == 12 or i == 25 or i == 38:
            suitchange += 1
            value = 0

        card = {
            "value": value,
            "sort_value": i,
            "suit": suits[suitchange],
            "face": cards[i]
        }
        dictCards.append(card)
        value += 1
    return dictCards


# def shuffledeck(hand):
#     random.shuffle(hand)
#     return hand


def sortcards(hand):
    hand.sort()
    return hand


def getcards(hand, amount, dictCards):
    for (i) in range(0, amount):
        toget = random.randint(0, len(dictCards) - 1)
        hand.append(dictCards.pop(toget))
    return hand


def samesuit(hand):
    r = True
    suit = hand[0].get("suit")
    for card in hand:
        if card.get("suit") != suit:
            r = False
    return r


def getsortedlist(hand, value):
    r = []
    for card in hand:
        r.append(card.get(value))
    r = sortcards(r)
    return r


def prettyprint(hand):
    r = []
    for card in hand:
        r.append(card.get("face"))
    return r


def debugprint(hand):
    r = []
    for card in hand:
        r.append(card.get("value"))
    return sorted(r)


# TODO edge case when the sequence is at the last 3 cards
def straight(hand):
    g = hand[0]
    for i in range(1, len(hand)):
        if g != hand[i] - 1:
            return False
        g += 1
    return True


def full(sorthand):
    threecheck = three(sorthand)
    if threecheck[0]:
        while threecheck[2] in sorthand:
            sorthand.remove(threecheck[2])
        if pair(sorthand)[0]:
            return True
    return False


def poker(sorthand):
    for i in range(0, len(sorthand) - 3):
        if sorthand[i] == sorthand[i + 1]:
            if sorthand[i + 1] == sorthand[i + 2]:
                if sorthand[i + 2] == sorthand[i + 3]:
                    return True


def three(sorthand):
    for i in range(0, len(sorthand) - 2):
        if sorthand[i] == sorthand[i + 1]:
            if sorthand[i + 1] == sorthand[i + 2]:
                return True, i + 2, sorthand[i + 2]
    return False, -1


def pair(sorthand):
    for i in range(0, len(sorthand) - 1):
        if sorthand[i] == sorthand[i + 1]:
            return True, i + 1
    return False, -1


def getpairs(sorthand):
    paircheck = pair(sorthand)
    value = -1
    if paircheck[0]:
        value = 0
        if paircheck[1] + 1 < len(sorthand) - 1:
            doublepair = pair(sorthand[paircheck[1]:])
            if doublepair[0]:
                # 2 Pair
                value = 1
    return value


def highCheck(sorthand):
    low = sorthand[0]
    for i in range(1, len(sorthand)):
        if low < sorthand[i]:
            low = sorthand[i]
    return low


def getresult(hand):
    sorthand = getsortedlist(hand, "value")
    nums = getsortedlist(hand, "sort_value")

    # straight flush
    if straight(nums) and samesuit(hand):
        # royal flush
        if sorthand[0] == 9 and sorthand[4] == 13:
            return 100
        else:
            return 90

    # poker
    if poker(sorthand):
        return 80

    # full
    if full(sorthand):
        return 70

    # Flush
    if samesuit(hand):
        return 60
    # straight
    if straight(nums):
        return 50
    # three
    if three(sorthand)[0]:
        return 40
    # Pair
    if getpairs(sorthand) == 1:
        return 30
    if getpairs(sorthand) == 0:
        return 20

    # High
    return highCheck(sorthand)


def getdummy(hand):
    for i in range(0, 2):
        hand.append(
            {
                "value": -1,
                "sort_value": -1,
                "suit": "-1",
                "face": "🂠"
            }

        )
    return hand
