roll = [1, 1, 3, 3, 1]

if 1 in roll:
    if roll[0]==1: print("1")
elif 2 in roll: print("2")
elif 3 in roll: print("3")
elif 4 in roll: print("4")
elif 5 in roll: print("5")
elif 6 in roll: print("6")

# display dice rolls
t=""
for i in roll: t+="["+str(i)+"] "
print(t)

i=0
if i!=7: print("True")
print(set(roll))
print(len(set(roll)))
