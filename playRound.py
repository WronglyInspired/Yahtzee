from random import *


def rollDice(roll, hold):
    i = 0
    for x in hold:
        if x == "0":
            roll[i] = randint(1, 6)
        i += 1
    return roll


def playRound():
    # initial roll
    input("Enter to Roll: ")
    roll = [0, 0, 0, 0, 0]
    roll = rollDice(roll, "00000")
    print(roll)
    rollNum = 1

    while 1 <= rollNum <= 2:
        player = input("Hold & Reroll OR Score")
        if len(player) == 1:  # if to score
            rollNum=3
        elif len(player) == 5:  # if to hold
            rollDice(roll, player)
            print(roll)
            rollNum+=1
        else:
            print("error invalid input")
    print("score category")


turn = 0
while turn < 13:
    playRound()
    turn += 1
