# roll dice
from random import *
roll=[0,0,0,0,0]


def rollDice(roll, hold):
    i=0
    for x in hold:
        if x=="0":
            roll[i]=randint(1,6)
        i+=1
    return roll

print(roll)
roll = rollDice(roll, "00000")
print(roll)
rollNum=1
while rollNum<3:
    hold=input("hold: ")
    roll = rollDice(roll, hold)
    print(roll)
    rollNum+=1
