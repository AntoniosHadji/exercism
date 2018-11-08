# Score categories
# Change the values as you see fit
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def four_of_a_kind_score(dice):
    for d in set(dice):
        if len(list(filter(lambda x: x == d, dice))) == 4:
            return sum(list(filter(lambda x: x == d, dice)))


SCORE_FUNCTION = {
    'yacht': lambda dice: 50,
    'ones': lambda dice: sum(list(filter(lambda x: x == 1, dice))),
    'twos': lambda dice: sum(list(filter(lambda x: x == 2, dice))),
    'threes': lambda dice: sum(list(filter(lambda x: x == 3, dice))),
    'fours': lambda dice: sum(list(filter(lambda x: x == 4, dice))),
    'fives': lambda dice: sum(list(filter(lambda x: x == 5, dice))),
    'sixes': lambda dice: sum(list(filter(lambda x: x == 6, dice))),
    'full_house': lambda dice: sum(dice),
    'four_of_a_kind': four_of_a_kind_score,
    'little_straight': lambda dice: 30,
    'big_straight': lambda dice: 30,
    'choice': lambda dice: sum(dice),
}


def score(dice, category):
    if category == LITTLE_STRAIGHT:
        if ((1 not in dice) or
           (len(dice) is not len(set(dice))) or
           (6 in dice)):
            return 0

    if category == FULL_HOUSE:
        for d in set(dice):
            length = len(list(filter(lambda x: x == d, dice)))
            if length not in [2, 3]:
                return 0

    if category == FOUR_OF_A_KIND:
        if len(set(dice)) == 1:
            return 4 * dice[0]

        count = set()
        for d in set(dice):
            count.add(len(list(filter(lambda x: x == d, dice))))
        if count != set([1, 4]):
            return 0

    if category == BIG_STRAIGHT:
        if 1 in dice:
            return 0

    if category == YACHT:
        if len(set(dice)) != 1:
            return 0

    return SCORE_FUNCTION[category](dice)
