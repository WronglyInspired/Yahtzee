roll = [2, 3, 1, 4, 2]

# if 1 in roll:
#     if roll[0]==1: print("1")
# elif 2 in roll: print("2")
# elif 3 in roll: print("3")
# elif 4 in roll: print("4")
# elif 5 in roll: print("5")
# elif 6 in roll: print("6")

# display dice rolls
# t=""
# for i in roll: t+="["+str(i)+"] "
# print(t)
#
# i=0
# if i!=7: print("True")
# print(set(roll))
# print(len(set(roll)))

# s = roll.count(1)and roll.count(2)and roll.count(3)and roll.count(4) or\
#     roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5) or\
#     roll.count(3)and roll.count(4)and roll.count(5)and roll.count(6)
# print(s)
# l = roll.count(1)and roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5) or\
#     roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5)and roll.count(6)
# print(l)
#


scores={
    "1": None,
    "2": None,
    "+3": None,
    "+4": None,
    "5": None,
    "6": None,
    "-3": None,
    "-4": None,
    "f": None,
    "s": None,
    "l": None,
    "c": None,
    "y": None
}
print(scores["1"])

if scores["y"]!=None:
    print("Filled")
else:
    print("None")
