# Yahtzee wip by WronglyInspired
from random import *

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


def categoryValid(ctgy, ctgys, testingExistence=False):
    if testingExistence == True and ctgys.get(ctgy) is not None:  # to test if ctgy exists
        return True
    if ctgys.get(ctgy) is not None and ctgys[ctgy]["value"] is None:
        return True
    return False


def awardPts(ctgy, ctgys, joker=False):
    if eval(ctgys[ctgy]["rule"]) or joker:
        x = eval(ctgys[ctgy]["pts"])
    else:
        x = 0
    return x


def rollDice(roll, hold):
    i = 0
    for x in hold:
        if x == "0":
            roll[i] = randint(1, 6)
        i += 1
    return roll


def playRound(ctgys, roll, last_round):
    rollNum = 0
    error = ""
    joker = False
    bonus = False
    # initial roll
    displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
    input("New rnd: ")
    roll = rollDice(roll, "00000")
    rollNum = 1

    while 1 <= rollNum <= 2:
        displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
        player = input("Hld or Scr: ")
        if len(player) == 1:  # if to score
            rollNum = 3
        elif len(player) == 5:  # if to hold
            roll = rollDice(roll, player)
            print(roll)
            rollNum += 1
        else:
            error = "<input err>"

    return roll, player


def scoreCategory(ctgys, player, roll):
    rollNum = 3
    error = ""
    last_round = "---"
    joker = False
    bonus = False
    if categoryValid(player, ctgys, True) and not categoryValid(player, ctgys):
        error = "<ctgy err>"
    while not categoryValid(player, ctgys):

        displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
        player = input("Score: ")

        if not categoryValid(player, ctgys):
            error = "<ctgy err>"

    if eval(ctgys["y"]["rule"]) and ctgys["y"]["value"] is not None:  # if the Yahtzee becomes a Joker
        joker = True
        # yahtzee bonus
        if 0 < ctgys["y"]["value"] <= 250:
            ctgys["y"]["value"] += 100
            bonus = True
        while True:
            # Free choice Joker rule
            if ctgys[str(playerDice[0])]["value"] is None:  # if the corresponding upper section box is empty
                if player == str(playerDice[0]):  # and player has chosen it, move on and score normally

                    roundPoints = awardPts(player, ctgys)
                    ctgys[player]["value"] = roundPoints
                    last_round = roundPoints

                    break
                else:
                    error = "<joker err>"  # otherwise throw error (which is nicer than giving them 0, as in original rules)
                    displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
                    player = input("Score joker time: ")
            else:  # JOKER
                roundPoints = awardPts(player, ctgys, True)
                ctgys[player]["value"] = roundPoints
                break

    # normal scoring
    else:
        roundPoints = awardPts(player, ctgys)
        ctgys[player]["value"] = roundPoints

    return ctgys, roundPoints


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
    best_ctgy = {"name": "-", "value": "--"}
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

print("==YAHTZEE============\nWelcome to Yahtzee. \nOfficial rules apply.\nSee rls & instrctns\nFor more help.\n")
input("Entr to bgn: ")
turn = 1
last_round = "---"
while turn <= 13:
    playerDice = [0, 0, 0, 0, 0]
    playRoundOutput = playRound(playerCtgys, playerDice, last_round)
    playerDice = playRoundOutput[0]
    scoreCategoryOutput = scoreCategory(playerCtgys, playRoundOutput[1], playerDice)
    playerCtgys = scoreCategoryOutput[0]
    last_round = scoreCategoryOutput[1]
    turn += 1

print("End of Game")
print(getScores(playerCtgys))


