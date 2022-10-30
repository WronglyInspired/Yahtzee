# Yahtzee wip by WronglyInspired
roll = [3, 1, 3, 1, 1]  # example roll

def findKind(num, roll, relate=">="):  # finds how many of a number in dice roll
    for i in range(1, 7):
        if relate == ">=" and roll.count(i) >= num:
            return True
        elif relate == "==" and roll.count(i) == num:
            return True
    return False


def findStraight(size, roll):  # finds small (4) or large (5) straights from a roll
    rollStr = str(set(roll)).strip("{}").replace(", ", "")  # code that converts a list to a set to a string.
    if size==4:
        return "1234" in rollStr or "2345" in rollStr or "3456" in rollStr
    elif size==5:
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

def categoryValid(input):
    if ctgys.get(input) is not None and ctgys[input]["value"] is None:
        return True
    return False

# def scrCtgy(ctgy, roll, rule=None):  # if rule is not set to True, we will assume there is no joker


def awardPts(roll, ctgy, joker=False):
    if ctgys[ctgy]["rule"] or joker:
        return ctgys[ctgy]["pts"]
    else:
        return 0



ctgys={ # ctgys is shorthand for categories
    "1": {"value": None, "row": "upper", "rule": True, "pts": roll.count(1) * 1},
    "2": {"value": None, "row": "upper", "rule": True, "pts": roll.count(2) * 2},
    "3": {"value": None, "row": "upper", "rule": True, "pts": roll.count(3) * 3},
    "4": {"value": None, "row": "upper", "rule": True, "pts": roll.count(4) * 4},
    "5": {"value": None, "row": "upper", "rule": True, "pts": roll.count(5) * 5},
    "6": {"value": None, "row": "upper", "rule": True, "pts": roll.count(6) * 6},
    "t": {"value": None, "row": "lower", "rule": findKind(3, roll), "pts": sum(roll)},  # triples / three of a kind
    "q": {"value": None, "row": "lower", "rule": findKind(4, roll), "pts": sum(roll)},  # quadruples / four of a kind
    "f": {"value": None, "row": "lower", "rule": findKind(2, roll, "==") and findKind(3, roll), "pts": 25},  # full house
    "s": {"value": None, "row": "lower", "rule": findStraight(4, roll), "pts": 30},  # small straight
    "l": {"value": None, "row": "lower", "rule": findStraight(5, roll), "pts": 40},  # large straight
    "c": {"value": None, "row": "lower", "rule": True, "pts": sum(roll)},  # chance
    "y": {"value": 50, "row": "lower", "rule": findKind(5, roll), "pts": 50},  # how to check this rule?
}
player = "f"


# print(ctgys[input]["rule"])
# print(ctgys[input]["pts"])
#
# print(categoryValid("y"))

if categoryValid(player):
    if ctgys["y"]["rule"] and ctgys["y"]["value"] is not None:  # if the Yahtzee becomes a Joker
        print("Joker Time")

        # yahtzee bonus
        if 0 < ctgys["y"]["value"] <= 250:
            ctgys["y"]["value"] += 100
            print("Yahtzee Bonus")

        # joker (Free choice Joker rule)
        if ctgys[str(roll[0])]["value"] is None:  # if the corresponding upper section box is empty
            if player == str(roll[0]):  # and player has chosen it, alg
                print("award points")
            else:
                print("error--must select corresponding upper section box")  # otherwise throw error (which is nicer than giving them 0)
        else:  # player can score in any box and rule = True
            ctgys[player]["value"] = awardPts(roll, player, True)
            print(f"{ctgys[player]['value']} points awarded to {player}")


    else:
        print("Normal scoring")
        ctgys[player]["value"] = awardPts(roll, player, True)
        print(f"{ctgys[player]['value']} points awarded to {player}")
else:
    print("ctgy err")

