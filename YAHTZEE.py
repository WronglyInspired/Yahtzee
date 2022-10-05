# Yahtzee wip by WronglyInspired
roll = [5, 1, 1, 3, 1] # example roll

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

ctgys={ # ctgys is shorthand for categories
    "1": {"value": None, "rule": True, "pts": roll.count(1) * 1},
    "2": {"value": None, "rule": True, "pts": roll.count(2) * 2},
    "3": {"value": None, "rule": True, "pts": roll.count(3) * 3},
    "4": {"value": None, "rule": True, "pts": roll.count(4) * 4},
    "5": {"value": None, "rule": True, "pts": roll.count(5) * 5},
    "6": {"value": None, "rule": True, "pts": roll.count(6) * 6},
    "t": {"value": None, "rule": findKind(3, roll), "pts": sum(roll)},  # triples / three of a kind
    "q": {"value": None, "rule": findKind(4, roll), "pts": sum(roll)},  # quadruples / four of a kind
    "f": {"value": None, "rule": findKind(2, roll, "==") and findKind(3, roll), "pts": 25},  # full house
    "s": {"value": None, "rule": findStraight(4, roll), "pts": 30},  # small straight
    "l": {"value": None, "rule": findStraight(5, roll), "pts": 40},  # large straight
    "c": {"value": None, "rule": True, "pts": sum(roll)},  # chance
    "y": {"value": None, "rule": True},  # how to check this rule?
}
input = "3"

ctgysKeys = list(ctgys.keys())  # converts keys of dictionaries into plan list
print(input in ctgysKeys)  # can then check to see if something is in that list
print(ctgys[input]["rule"])
print(ctgys[input]["pts"])

