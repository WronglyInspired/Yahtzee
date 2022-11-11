# Yahtzee for Casio fx-9860GIII by WronglyInspired. Runs on Python 3+, and MicroPython 1.9.4
from random import randint
def findKind(num, roll, relate=">="):  # finds how many of a number in dice roll
    for i in range(1, 7):
        if relate == ">=" and roll.count(i) >= num:
            return True
        elif relate == "==" and roll.count(i) == num:
            return True
    return False
def findStraight(size, roll):  # finds small (4) or large (5) straights from a roll
    rollStr = str(sorted(set(roll))).strip("{}").replace(", ", "")  # code that converts a list to a set to a string.
    if size == 4:
        return "1234" in rollStr or "2345" in rollStr or "3456" in rollStr
    elif size == 5:
        return "12345" in rollStr or "23456" in rollStr
    else:
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
    rollNum, error, joker, bonus = 0, "", False, False
    # initial roll
    displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
    input("New rnd: ")
    roll, rollNum = rollDice(roll, "00000"), 1
    while 1 <= rollNum <= 2:
        displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
        player = input("Hld or Scr: ").upper()
        if len(player) == 1:  # if to score
            rollNum = 3
        elif len(player) == 5:  # if to hold
            roll = rollDice(roll, player)
            rollNum += 1
        else:
            error = "<input err>"
    return roll, player
def scoreCategory(ctgys, player, roll):
    rollNum, error, last_round, joker, bonus = 3, "", "---", False, False
    if categoryValid(player, ctgys, True) and not categoryValid(player, ctgys):
        error = "<ctgy err>"
    while not categoryValid(player, ctgys):
        displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
        player = input("Score: ").upper()
        if not categoryValid(player, ctgys):
            error = "<ctgy err>"
    if eval(ctgys["Y"]["rule"]) and ctgys["Y"]["value"] is not None:  # if the Yahtzee becomes a Joker
        joker = True
        if 0 < ctgys["Y"]["value"] <= 250:  # yahtzee bonus
            ctgys["Y"]["value"] += 100
            bonus = True
        while True: # Free choice joker rule
            if ctgys[str(plyrDice[0])]["value"] is None:  # if the corresponding upper section box is empty
                if player == str(plyrDice[0]):  # and player has chosen it, move on and score normally
                    roundPoints = awardPts(player, ctgys)
                    ctgys[player]["value"] = roundPoints
                    break
                else:
                    error = "<joker err>"  # otherwise throw error
                    displayScreen(ctgys, roll, rollNum, error, last_round, joker, bonus)
                    player = input("Scr: ").upper()
            else:  # JOKER
                roundPoints = awardPts(player, ctgys, True)
                ctgys[player]["value"] = roundPoints
                break
    else:  # normal scoring
        roundPoints = awardPts(player, ctgys)
        ctgys[player]["value"] = roundPoints
    return ctgys, roundPoints
def getScores(ctgys):
    upper_scores, lower_scores = [], []
    for key, v in ctgys.items():  # upper row
        if v["row"] == "upper":
            upper_scores.append(v["value"]) if v["value"] is not None else upper_scores.append(0)
    upper_scores = sum(upper_scores)
    upper_bonus = 35 if upper_scores >= 63 else 0  # upper row bonus
    for key, v in ctgys.items():  # lower row
        if v["row"] == "lower":
            lower_scores.append(v["value"]) if v["value"] is not None else lower_scores.append(0)
    lower_scores = sum(lower_scores)
    total_score = upper_scores + upper_bonus + lower_scores
    return upper_scores, upper_bonus, lower_scores, total_score
def displayScreen(ctgys, roll, rollNum, error="", last_round="---", joker=False, bonus=False):  # roll, rollNum):
    scores = getScores(ctgys)
    upper_scores, total_score = scores[0], scores[3]
    best_ctgy = {"name": "-", "value": 0}
    for x in "123456QTFSLCY":
        if awardPts(x, ctgys) > best_ctgy["value"] and categoryValid(x, ctgys):
            best_ctgy["name"], best_ctgy["value"] = x, awardPts(x, ctgys)
    upper_display, lower_display = "123456", "TQFSLCY"
    for i in upper_display:
        upper_display += i.upper() if ctgys[i.upper()]["value"] is None else "-"
    for i in lower_display:
        lower_display += i.upper() if ctgys[i.upper()]["value"] is None else "-"
    upper_display, lower_display = upper_display[6:], lower_display[7:]
    line4_display = "  "
    line4_display += "{JOKER}  " if joker else "         "
    line4_display += "{BONUS}" if bonus else "       "
    print("==YAHTZEE=====Scr:{:0>3}".format(total_score))
    print(" {} ={:0>3}  lst:{:0>3}".format(upper_display, upper_scores, last_round))
    print(" {}   bst:{}:{:0>2}".format(lower_display, best_ctgy['name'].upper(), best_ctgy['value']))
    print(line4_display)
    print(" [{}] [{}] [{}] [{}] [{}]".format(roll[0],roll[1],roll[2],roll[3],roll[4]))
    print(" {:13} roll:{}".format(error,rollNum))
plyrCtgys = {"1": {"value": None, "row": "upper", "rule": "True", "pts": "plyrDice.count(1) * 1"},"2": {"value": None,
    "row": "upper", "rule": "True", "pts": "plyrDice.count(2) * 2"},"3": {"value": None, "row": "upper", "rule":
    "True", "pts": "plyrDice.count(3) * 3"},"4": {"value": None, "row": "upper", "rule": "True", "pts":
    "plyrDice.count(4) * 4"},"5": {"value": None, "row": "upper", "rule": "True", "pts": "plyrDice.count(5) * 5"},
    "6": {"value": None, "row": "upper", "rule": "True", "pts": "plyrDice.count(6) * 6"},"T": {"value": None, "row":
    "lower", "rule": "findKind(3, plyrDice)", "pts": "sum(plyrDice)"},"Q": {"value": None, "row": "lower", "rule":
    "findKind(4, plyrDice)", "pts": "sum(plyrDice)"},"F": {"value": None, "row": "lower", "rule": "findKind(2, ply"
    "rDice, '==') and findKind(3, plyrDice)","pts": "25"},"S": {"value": None, "row": "lower", "rule": "findStraight"
    "(4, plyrDice)", "pts": "30"},"L": {"value": None, "row": "lower", "rule": "findStraight(5, plyrDice)", "pts":
    "40"},"C": {"value": None, "row": "lower", "rule": "True", "pts": "sum(plyrDice)"},"Y": {"value": None, "row":
    "lower", "rule": "findKind(5, plyrDice)", "pts": "50"}}
print("==YAHTZEE============\nWelcome to Yahtzee. \nOfficial rules apply.\nSee README\nFor more help.\n")
input("Entr to bgn: ")
turn, last_round = 1, "---"
while turn <= 13:
    plyrDice = [0, 0, 0, 0, 0]
    playRoundOutput = playRound(plyrCtgys, plyrDice, last_round)
    plyrDice = playRoundOutput[0]
    scoreCategoryOutput = scoreCategory(plyrCtgys, playRoundOutput[1], plyrDice)
    plyrCtgys = scoreCategoryOutput[0]
    last_round = scoreCategoryOutput[1]
    turn += 1
player_scores = getScores(plyrCtgys)
getScores(plyrCtgys)
a, b, c, d = "Upper row:", "Upper row bonus:", "Lower row:", "TOTAL SCORE:"
print("==YAHTZEE=======End==\n{:17} {:0>3}\n{:17} {:0>3}\n{:17} {:0>3}\n{:15} -{:0>3}-\n"
      .format(a,player_scores[0],b,player_scores[1],c,player_scores[2],d,player_scores[3]))
input("Ty! Rload to ply agn")
