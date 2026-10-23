from random import choice

computer = choice([-1,0,1])
you = input("Enter your choice: ")
youDict = {'s': 1, 'w':-1, 'g':0}
reverseDict = {1: "Snake", -1:"Water", 0:"Gun"}

user = youDict[you]

print(f"You chose {reverseDict[user]}\nComputer chose {reverseDict[computer]}")

if (computer == user):
    print("Draw")

else:
    if (computer==-1 and user==1):
        print("You Win!")
    elif (computer==-1 and user==0):
        print("You Lose!")
    elif (computer==1 and user==-1):
        print("You Lose!")
    elif (computer==1 and user==0):
        print("You Win!")
    elif (computer==0 and user==-1):
        print("You Win!")
    elif (computer==0 and user==1):
        print("You Lose!")
    else:
        print("Something went wrong")
