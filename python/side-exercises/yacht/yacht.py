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


def count_dice(dice):
    counts = {}
    for d in dice:
        if d in counts:
            counts[d] += 1
        else:
            counts[d] = 1
    return counts


def four_of_a_kind_score(dice):
    counts = count_dice(dice)
    for d, c in counts.items():
        if c == 4:
            return c*d


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
        if 1 not in dice:
            return 0
        if len(dice) is not len(set(dice)):
            return 0

    if category == FULL_HOUSE:
                pass

    return SCORE_FUNCTION[category](dice)
