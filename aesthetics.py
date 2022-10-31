# Yahtzee wip by WronglyInspired
from random import *

playerDice = [0, 0, 0, 0, 0]


def categoryValid(ctgy, ctgys, testingExistence=False):
    if testingExistence == True and ctgys.get(ctgy) is not None:  # to test if ctgy exists
        return True
    if ctgys.get(ctgy) is not None and ctgys[ctgy]["value"] is None:
        return True
    return False


# return upper_scores, upper_bonus, lower_scores, total_score
def getScores(ctgys):
    upper_scores = []
    lower_scores = []
    # upper row
    for key, v in ctgys.items():
        if v["row"] == "upper":
            if v["value"] is None:
                upper_scores.append(0)
            else:
                upper_scores.append(v["value"])
    upper_scores = sum(upper_scores)
    # upper row bonus
    if upper_scores >= 63:
        upper_bonus = 35
    else:
        upper_bonus = 0
    # lower row
    for key, v in ctgys.items():
        if v["row"] == "lower":
            if v["value"] is None:
                lower_scores.append(0)
            else:
                lower_scores.append(v["value"])
    lower_scores = sum(lower_scores)
    total_score = upper_scores + upper_bonus + lower_scores
    return upper_scores, upper_bonus, lower_scores, total_score


# error length can be max length 13 including <>
def displayScreen(ctgys, roll, rollNum, error="", last_round="---", joker=False, bonus=False):  # roll, rollNum):
    scores = getScores(ctgys)
    upper_scores = scores[0]
    total_score = scores[3]
    best_ctgy = {"name": "n", "value": "--"}
    # best_ctgy = findBestCtgy(roll)
    upper_display = ""
    lower_display = ""
    for count, value in enumerate(ctgys.keys()):
        if count < 6:
            upper_display += value.upper() if ctgys[value]["value"] is None else "-"
        elif count < 12:
            lower_display += value.upper() if ctgys[value]["value"] is None else "-"
        elif count < 13:
            lower_display += " Y" if ctgys[value]["value"] is None else " -"
    line4_display = "  "
    line4_display += "{JOKER}  " if joker else "         "
    line4_display += "{BONUS}" if bonus else "       "
    print(f"==YAHTZEE=====Scr:{total_score:0>3}")
    print(f" {upper_display} ={upper_scores:0>3}  lst:{last_round:0>3}")
    print(f" {lower_display}   bst:{best_ctgy['name'].upper()}:{best_ctgy['value']:0>2}")
    print(line4_display)
    print(f" [{roll[0]}] [{roll[1]}] [{roll[2]}] [{roll[3]}] [{roll[4]}]")
    print(f" {error:13} roll:{rollNum}")


playerCtgys = {  # ctgys is shorthand for categories
    "1": {"value": None, "row": "upper", "rule": "True", "pts": "playerDice.count(1) * 1"},
    "2": {"value": None, "row": "upper", "rule": "True", "pts": "playerDice.count(2) * 2"},
    "3": {"value": None, "row": "upper", "rule": "True", "pts": "playerDice.count(3) * 3"},
    "4": {"value": None, "row": "upper", "rule": "True", "pts": "playerDice.count(4) * 4"},
    "5": {"value": None, "row": "upper", "rule": "True", "pts": "playerDice.count(5) * 5"},
    "6": {"value": None, "row": "upper", "rule": "True", "pts": "playerDice.count(6) * 6"},
    "t": {"value": None, "row": "lower", "rule": "findKind(3, playerDice)", "pts": "sum(playerDice)"},
    # triples / three of a kind
    "q": {"value": None, "row": "lower", "rule": "findKind(4, playerDice)", "pts": "sum(playerDice)"},
    # quadruples / four of a kind
    "f": {"value": None, "row": "lower", "rule": "findKind(2, playerDice, '==') and findKind(3, playerDice)",
          "pts": "25"},
    # full house
    "s": {"value": None, "row": "lower", "rule": "findStraight(4, playerDice)", "pts": "30"},  # small straight
    "l": {"value": None, "row": "lower", "rule": "findStraight(5, playerDice)", "pts": "40"},  # large straight
    "c": {"value": None, "row": "lower", "rule": "True", "pts": "sum(playerDice)"},  # chance
    "y": {"value": None, "row": "lower", "rule": "findKind(5, playerDice)", "pts": "50"},  # how to check this rule?
}

rollNum = 1
error = "             "
# error = "<ctgy err>"
displayScreen(playerCtgys, playerDice, rollNum, error, last_round, joker, bonus)
input("Hld or Scr: ")


