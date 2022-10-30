# Yahtzee wip by WronglyInspired
playerDice = [0, 0, 0, 0, 0]


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


def awardPts(ctgy, joker=False):
    if ctgys[ctgy]["rule"] or joker:
        x = ctgys[ctgy]["pts"]
        print("you get", x)
    else:
        print("nothing, you get", 0)





def playRound(roll):
    roll = [1, 2, 3, 4, 4]
    return roll


def scoreCategory():
    player = "4"
    print("Normal scoring")
    print(ctgys[player]["pts"])
    awardPts(player)
    print(f"{ctgys[player]['value']} points awarded to {player}")


playerDice = [1, 2, 3, 4, 4]
playerDice = playRound(playerDice)
ctgys = {  # ctgys is shorthand for categories
    "1": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(1) * 1},
    "2": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(2) * 2},
    "3": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(3) * 3},
    "4": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(4) * 4},
    "5": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(5) * 5},
    "6": {"value": None, "row": "upper", "rule": True, "pts": playerDice.count(6) * 6},
    "t": {"value": None, "row": "lower", "rule": findKind(3, playerDice), "pts": sum(playerDice)},  # triples / three of a kind
    "q": {"value": None, "row": "lower", "rule": findKind(4, playerDice), "pts": sum(playerDice)},  # quadruples / four of a kind
    "f": {"value": None, "row": "lower", "rule": findKind(2, playerDice, "==") and findKind(3, playerDice), "pts": 25},  # full house
    "s": {"value": None, "row": "lower", "rule": findStraight(4, playerDice), "pts": 30},  # small straight
    "l": {"value": None, "row": "lower", "rule": findStraight(5, playerDice), "pts": 40},  # large straight
    "c": {"value": None, "row": "lower", "rule": True, "pts": sum(playerDice)},  # chance
    "y": {"value": None, "row": "lower", "rule": findKind(5, playerDice), "pts": 50},  # how to check this rule?
}
scoreCategory()

