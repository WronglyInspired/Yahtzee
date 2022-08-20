# code that asks and evaluates player input
# test and example code for things related to categories
roll = [5, 1, 1, 3, 1] # example roll

##########################################################################################
def findKind(num, roll, relate=">="):
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
    "t": {"value": None, "rule": findKind(3, roll), "pts": sum(roll)},
    "q": {"value": None, "rule": findKind(4, roll), "pts": sum(roll)},
    "f": {"value": None, "rule": findKind(2, roll, "==") and findKind(3, roll), "pts": 25},
    "s": {"value": None, "rule": findStraight(4, roll), "pts": 30},
    "l": {"value": None, "rule": findStraight(5, roll), "pts": 40},
    "c": {"value": None, "rule": True, "pts": sum(roll)},
    "y": {"value": None, "rule": True},  # how to check this rule?
}
ans = "t"

ctgysKeys = list(ctgys.keys())  # converts keys of dictionaries into plan list
print(ans in ctgysKeys)  # can then check to see if something is in that list
print(ctgys[ans]["rule"])
print(ctgys[ans]["pts"])

#######################################################################

def askPlayer(rollNum, prompt=""):
    print(prompt)
    if rollNum==0:
        input("Enter to Roll: ")
    elif rollNum<3:
        ans=input("Hold or Score: ").lower()
        if len(ans)==5:  # hold
            return ans  # return string for hold
        elif len(ans)==1:  # ctgy
            if ans in list(ctgys.keys()):  # if ctgy exists
                print("ctgy exists")
            else:
                askPlayer(rollNum, "<ctgy err>")
        else:
            askPlayer(rollNum, "<input err>")
    else:
        ans=input("Slct Ctgy 2 Scr: ").lower()
        if len(ans)!=1:
            askPlayer(rollNum, "<input err>")
        elif ans not in list(ctgys.keys()):
            askPlayer(rollNum, "<ctgy err>")
        else:
            print("ctgy exists")

def entrScr(roll, ctgy):
    if len(set(roll))==1:  # if yahtzee
        if ctgy=="y":  # if player entered into yahtzee category

        elif ctgys["y"]!=None:  # if yahtzee filled
            joker=True
        elif ctgy!="y":  # if


askPlayer(2)
