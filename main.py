import random
''' s for Snake
w for Water
g for Gun'''

computer = random.choice(["s", "w", "g"])
print("Welcome to the Snake Water Gun game!")
print("Rules are simple\nsnake drinks water, water damages gun and gun kills snake")
print("So choose wisely")
print("s for snake\nw for water\ng for gun")
print("Would you like to play the game?")
if(input("Enter y for yes and n for no : ") == "n"):
    print("Thank you for visiting!")
    exit()

you = input("Enter your choice : ")

reversedict = {"s" : "snake", "w" : "water", "g" : "gun"}

print(f"you chose :{reversedict[you]}\n computer chose :{reversedict[computer]}")

if(computer == you):
    print("Its draw!")
else:
    if(computer == "s" and you == "w"):
        print("You lose!")
    elif(computer == "g" and you == "s"):
        print("You win!")
    elif(computer == "g" and you == "w"):
        print("You lose!")
    elif(computer == "w" and you == "g"):
        print("You win!")
    elif(computer == "s" and you == "g"):
        print("You win!")
    elif(computer == "w" and you == "s"):
        print("You win!")
    else:
        print("Something went wrong!")
    