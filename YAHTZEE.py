# Yahtzee logic by WronglyInspired
# to add: Yahtzee Bonus, Upper Row Bonus,
roll = [4, 4, 4, 4, 4]
if len(set(roll))==1:
    isYahtzee=True

scores = {"1": None, "2": None, "+3": None, "+4": None, "5": None, "6": None,
          "-3": None, "-4": None, "f": None, "s": None, "l": None, "c": None, "y": None}

ctgy = "y".lower()


# ctgy = input("Category: ").lower()
def findKind(num, roll, relate=">="):
    for i in range(1, 7):
        if relate == ">=" and roll.count(i) >= num:
            return True
        elif relate == "==" and roll.count(i) == num:
            return True
    return False


def scrCtgy(ctgy, roll): # takes user input for ctgy and their roll, and decides what points to add. (Maybe rename to do all
    # input processing)
    if ctgy in ("1", "+1") and scores["1"] != None:
        scr = roll.count(1) * 1
        scores["1"]=scr
    elif ctgy in ("2", "+2") and scores["2"] != None:
        scr = roll.count(2) * 2
        scores["2"]=scr
    elif ctgy == "+3" and scores["+3"] != None:
        scr = roll.count(3) * 3
        scores["+3"]=scr
    elif ctgy == "+4" and scores["+4"] != None:
        scr = roll.count(4) * 4
        scores["+4"]=scr
    elif ctgy in ("5", "+5") and scores["5"] != None:
        scr = roll.count(5) * 5
        scores["5"]=scr
    elif ctgy in ("6", "+6") and scores["6"] != None:
        scr = roll.count(6) * 6
        scores["6"]=scr
    elif ctgy == "-3" and scores["-3"] != None and findKind(3, roll):
        scr = sum(roll)  # 3 of a kind
        scores["-3"]=scr
    elif ctgy == "-4" and scores["-4"] != None and findKind(4, roll):
        scr = sum(roll)  # 4 of a kind
        scores["-4"]=scr
    elif ctgy == "f" and scores["f"] != None and findKind(2, roll, "==") and findKind(3, roll):
        scr = 25  # full house
        scores["f"]=scr
    elif ctgy == "s" and scores["s"] != None and roll.count(1) and roll.count(2) and roll.count(3) and roll.count(4) or \
            roll.count(2) and roll.count(3) and roll.count(4) and roll.count(5) or \
            roll.count(3) and roll.count(4) and roll.count(5) and roll.count(6):
        scr = 30  # small straight
        scores["s"]=scr
    elif ctgy == "l" and scores["l"] != None and roll.count(1) and roll.count(2) and roll.count(3) and roll.count(4) and \
            roll.count(5) or roll.count(2) and roll.count(3) and roll.count(4) and roll.count(5) and roll.count(6):
        scr = 40  # large straight
        scores["l"]=scr
    elif ctgy == "c" and scores["c"] != None:
        scr = sum(roll)
        scores["c"]=scr
    elif ctgy == "y" and scores["y"] != None and isYahtzee==True:
        scr = 50
        scores["y"]=scr
    else:
        scr = 0
    return scr


# upr = 0 # upper row sum

# print(findKind(3,roll))
print(scrCtgy(ctgy, roll))
