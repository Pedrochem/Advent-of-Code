from enum import Enum

class Hand(Enum):
    FIVE_KIND = 6
    FOUR_KIND = 5
    FULL_HOUSE = 4
    THREE_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


def get_type(hand):
    dups = set()
    unique = set()
    n_jokes=0
    for card in hand:
        if card == 'J':
            n_jokes +=1
            continue
        if card in unique:
            dups.add(card)
        else:
            unique.add(card)
    
    size_unique = len(unique)
    size_dups = len(dups)
    if size_dups==0 and n_jokes>0:
        size_dups+=1
    if size_unique == 0:
        size_unique+=1

    match size_unique,size_dups:
        case 1,1:
            return Hand.FIVE_KIND
        case 2,1:
            return Hand.FOUR_KIND
        case 2,2:
            return Hand.FULL_HOUSE
        case 3,1:
            return Hand.THREE_KIND
        case 3,2:
            return Hand.TWO_PAIR
        case 4,1:
            return Hand.ONE_PAIR
        case 5,0:
            return Hand.HIGH_CARD
    return 0

def get_numbered(hand):
    card_2_num = {
        'T': 10,
        'J': 0,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    res = []
    for card in hand:
        if card in card_2_num.keys():
            card_num = card_2_num[card]
        else:
            card_num = int(card)
        res.append(card_num)
    
    return res


with open("full_input.txt") as f:
    lines = [line.rstrip() for line in f]
    hands = []
    for line in lines:
        hand, bid = line.split()
        h_type = get_type(hand)
        hand_num = get_numbered(hand)

        hands.append((hand_num,h_type,hand,int(bid)))
    
    hands.sort(key= lambda x: (x[1].value, x[0]))
    
    # print(hands)
    for h in hands:
        print(h)
    
    res = 0
    for i, hand in enumerate(hands):
        res += (i+1) * hand[-1]
    
    print(res)