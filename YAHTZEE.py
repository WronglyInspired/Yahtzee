roll = [2, 2, 2, 3, 3]
ctgy="f".lower()
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
    else: scr=0
    return scr

# print(findKind(3,roll))
print(scrCtgy(ctgy,roll))
