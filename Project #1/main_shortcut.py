
'''
1 for snake
-1 for water 
0 for gun

'''
import random

computer = random.choice([1, -1, 0])
youStr = input("Enter you choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

if youStr not in youDict:
    print("Invalid choice! Please enter s, w, or g")
    exit()

you = youDict[youStr]

print(f"you chose {reverseDict[you]}\nComputer choice  {reverseDict[computer]}")

if computer == you:
    print("Match Draw")

else:
    if ((computer - you) == -1) or ((computer - you) == 2):
        print("You lose")
    else:
        print("You Win")
   