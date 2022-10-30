# Yahtzee wip by WronglyInspired
from random import *

playerDice = [0, 0, 0, 0, 0]
# roll = [3, 1, 3, 1, 1]  # example roll


def findKind(num, roll, relate=">="):  # finds how many of a number in dice roll
    for i in range(1, 7):
        if relate == ">=" and roll.count(i) >= num:
            return True
        elif relate == "==" and roll.count(i) == num:
            return True
    return False


def findStraight(size, roll):  # finds small (4) or large (5) straights from a roll
    rollStr = str(set(roll)).strip("{}").replace(", ", "")  # code that converts a list to a set to a string.
    if size == 4:
        return "1234" in rollStr or "2345" in rollStr or "3456" in rollStr
    elif size == 5:
        return "12345" in rollStr or "23456" in rollStr
    else:
        print("<err finding straight>")  # error/bug prevention
        return False


# def categoryValid(input):
#     ctgysKeys = list(ctgys.keys())  # converts keys of dictionaries into plan list
#     if input in ctgysKeys:  # can then check to see if something is in that list
#         if ctgys[input]["value"] is None:
#             return True
#     return False

def categoryValid(ctgy, ctgys):
    if ctgys.get(ctgy) is not None and ctgys[ctgy]["value"] is None:
        return True
    return False


def awardPts(ctgy, ctgys, joker=False):
    print("awardPts()", ctgys)
    if ctgys[ctgy]["rule"] or joker:
        x = ctgys[ctgy]["pts"]
        print("you get", x)
    else:
        print("nothing, you get", 0)


def rollDice(roll, hold):
    i = 0
    for x in hold:
        if x == "0":
            roll[i] = randint(1, 6)
        i += 1
    return roll


def playRound(roll):
    # initial roll
    input("Enter to Roll new round: ")
    roll = rollDice(roll, "00000")
    print(roll)
    rollNum = 1

    while 1 <= rollNum <= 2:
        player = input("Hold & Reroll OR Score")
        if len(player) == 1:  # if to score
            rollNum = 3
        elif len(player) == 5:  # if to hold
            roll = rollDice(roll, player)
            print(roll)
            rollNum += 1
        else:
            print("error invalid input")

    return roll


def scoreCategory(ctgys):
    print("scoreCategory()", ctgys)
    player = None
    while not categoryValid(player, ctgys):
        player = input("Score: ")
        if categoryValid(player, ctgys):
            if ctgys["y"]["rule"] and ctgys["y"]["value"] is not None:  # if the Yahtzee becomes a Joker
                print("Joker Time")

                # yahtzee bonus
                if 0 < ctgys["y"]["value"] <= 250:
                    ctgys["y"]["value"] += 100
                    print("Yahtzee Bonus")

                # joker (Free choice Joker rule)
                if ctgys[str(playerDice[0])]["value"] is None:  # if the corresponding upper section box is empty
                    if player == str(playerDice[0]):  # and player has chosen it, alg
                        print("award points")
                    else:
                        print("error--must select corresponding upper section box")  # otherwise throw error (which is nicer than giving them 0)
                else:  # player can score in any box and rule = True
                    awardPts(player, ctgys, True)
                    print(f"{ctgys[player]['value']} points awarded to {player}")

            else:
                print("Normal scoring")
                print(ctgys[player]["pts"])
                awardPts(player, ctgys)
                print(f"{ctgys[player]['value']} points awarded to {player}")
        else:
            print("ctgy err")
    print("returning scoreCategory()", ctgys)
    return ctgys


playerCtgys = {  # ctgys is shorthand for categories
    "1": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(1) * 1},
    "2": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(2) * 2},
    "3": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(3) * 3},
    "4": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(4) * 4},
    "5": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(5) * 5},
    "6": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(6) * 6},
    "t": {"value": None, "row": "lower", "rule": findKind(3, playerDice), "pts": sum(playerDice)},  # triples / three of a kind
    "q": {"value": None, "row": "lower", "rule": findKind(4, playerDice), "pts": sum(playerDice)},  # quadruples / four of a kind
    "f": {"value": None, "row": "lower", "rule": findKind(2, playerDice, "==") and findKind(3, playerDice), "pts": 25},
    # full house
    "s": {"value": None, "row": "lower", "rule": findStraight(4, playerDice), "pts": 30},  # small straight
    "l": {"value": None, "row": "lower", "rule": findStraight(5, playerDice), "pts": 40},  # large straight
    "c": {"value": None, "row": "lower", "rule": True, "pts": sum(playerDice)},  # chance
    "y": {"value": 50, "row": "lower", "rule": findKind(5, playerDice), "pts": 50},  # how to check this rule?
}

# !!the problem is that the pts part of ctgys is evaluating straight away, until waiting until dice has been rolled for evaluating
turn = 0
while turn < 13:
    playerDice = [0, 0, 0, 0, 0]
    playerDice = playRound(playerDice)
    print("pCategories before", playerCtgys)
    playerCtgys = scoreCategory(playerCtgys)
    print("pCategories after", playerCtgys)
    turn += 1
