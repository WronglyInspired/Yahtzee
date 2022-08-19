# Yahtzee logic by WronglyInspired
roll = [4, 4, 4, 4, 4]
ctgy="y".lower()
#ctgy = input("Category: ").lower()
def findKind(num, roll, relate=">="):
    for i in range(1, 7):
        if relate==">=" and roll.count(i)>=num: return True
        elif relate=="==" and roll.count(i)==num: return True
    return False

def scrCtgy(ctgy,roll):
    if ctgy in("1","+1"): scr=roll.count(1)*1
    elif ctgy in("2","+2"): scr=roll.count(2)*2
    elif ctgy=="+3": scr=roll.count(3)*3
    elif ctgy=="+4": scr=roll.count(4)*4
    elif ctgy in("5","+5"): scr=roll.count(5)*5
    elif ctgy in("6","+6"): scr=roll.count(6)*6
    elif ctgy=="-3" and findKind(3,roll): scr=sum(roll) #3 of a kind
    elif ctgy=="-4" and findKind(4,roll): scr=sum(roll) #4 of a kind
    elif ctgy=="f" and findKind(2, roll, "==") and findKind(3,roll): scr=25 #full house
    elif ctgy=="s" and roll.count(1)and roll.count(2)and roll.count(3)and roll.count(4) or\
        roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5) or\
        roll.count(3)and roll.count(4)and roll.count(5)and roll.count(6): scr=30 #small straight
    elif ctgy=="l" and roll.count(1)and roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5) or\
        roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5)and roll.count(6): scr=40 #large straight
    elif ctgy=="c": scr=sum(roll)
    elif ctgy=="y" and findKind(5,roll): scr=50
    else: scr=0
    return scr

# print(findKind(3,roll))
print(scrCtgy(ctgy,roll))
