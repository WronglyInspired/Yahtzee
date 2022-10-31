# roll = [5, 3, 4, 3, 2]
#
# # if 1 in roll:
# #     if roll[0]==1: print("1")
# # elif 2 in roll: print("2")
# # elif 3 in roll: print("3")
# # elif 4 in roll: print("4")
# # elif 5 in roll: print("5")
# # elif 6 in roll: print("6")
#
# # display dice rolls
# # t=""
# # for i in roll: t+="["+str(i)+"] "
# # print(t)
# #
# # i=0
# # if i!=7: print("True")
# # print(set(roll))
# # print(len(set(roll)))
#
# # s = roll.count(1)and roll.count(2)and roll.count(3)and roll.count(4) or\
# #     roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5) or\
# #     roll.count(3)and roll.count(4)and roll.count(5)and roll.count(6)
# # print(s)
# # l = roll.count(1)and roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5) or\
# #     roll.count(2)and roll.count(3)and roll.count(4)and roll.count(5)and roll.count(6)
# # print(l)
# #
#
# def findKind(num, roll, relate=">="):
#     for i in range(1, 7):
#         if relate == ">=" and roll.count(i) >= num:
#             return True
#         elif relate == "==" and roll.count(i) == num:
#             return True
#     return False
#
#
# def findStraight(size, roll):  # finds small (4) or large (5) straights from a roll
#     rollStr = str(set(roll)).strip("{}").replace(", ", "")  # code that converts a list to a set to a string.
#     if size==4:
#         return "1234" in rollStr or "2345" in rollStr or "3456" in rollStr
#     elif size==5:
#         return "12345" in rollStr or "23456" in rollStr
#     else:
#         print("<err: straight size not possible>")  # error/bug prevention
#         return False
#
ctgys={ # categories shorthand
    "1": {"value": None, "rule": True},
    "2": {"value": None, "rule": True},
    "3": {"value": None, "rule": True},
    "4": {"value": None, "rule": True},
    "5": {"value": None, "rule": True},
    "6": {"value": None, "rule": True},
    "t": {"value": None, "rule": True},
    "q": {"value": None, "rule": True},
    "f": {"value": None, "rule": True},
    "s": {"value": None, "rule": True},
    "l": {"value": None, "rule": True},
    "c": {"value": None, "rule": True},
    "y": {"value": None, "rule": True},  # how to check this rule?
}
# # ctgysKeys = list(ctgys.keys())  # converts keys of dictionaries into plan list
# # print("t" in ctgysKeys)  # can then check to see if something is in that list
# #
# # print(ctgys["l"]["rule"])
# #
#
# # rollStr = str(set(roll)).strip("{}").replace(", ", "")  # code that converts a list to a set to a string.
# # print(rollStr)
# # print("1234" in rollStr or "2345" in rollStr or "3456" in rollStr)
# # print("12345" in rollStr or "23456" in rollStr)
#
# # print(scores["1"])
# #
# # if scores["y"]!=None:
# #     print("Filled")
# # else:
# #     print("None")
#
# # input(">>> ")
#
# # def iman():
# #     i = 0
# #     while i < 3:
# #         print(i)
# #         i += 1
# #     print("end")
# #
# # iman()
# # print("finish")
#
# # playerDice = [6, 6, 2, 1, 3]
# # x = "playerDice.count(6) * 6"
# # print(eval(x))
# x = 50
# print(eval("50"))

print(list(ctgys.keys()))
