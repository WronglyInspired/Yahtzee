# roll dice
from random import *
dice=[0, 0, 0, 0, 0]


def rollDice(roll, hold):
    i=0
    for x in hold:
        if x=="0":
            roll[i]=randint(1,6)
        i+=1
    return roll

print(dice)
dice = rollDice(dice, "00000")
print(dice)
rollNum=1
while rollNum<3:
    hold=input("hold: ")
    dice = rollDice(dice, hold)
    print(dice)
    rollNum+=1
