import random
# import randint   
# Rock Paper Scissors Game
# Introduction
print("Welcome!")
print("The game we are going to play is 'Rock Paper Scissor'")
print("rules:")
print("Scissor cuts Paper, Paper wraps Rock, and Rock smashes Scissor.")
print("Type 'r' for Rock, 'p' for Paper, 's' for Scissor.")
print('So, would you like to play the game?')

# Decision upto user
game = (input("Enter the 'y' to proceed or 'n' to exit : ")).lower()
# Every variable are assigned for game
if (game == "n"):
    print("Thank you fro visiting!")
    exit()
    # Only (y/n) to proceed otherwise the game will exit itself
if (game != 'y' and 'n'):
    print("Enter only (y/n)")
    exit()

 # keywords with its values to allow the game to be played       
keywords = {"r" : "Rock", "s" : "Scissor", "p" : "Papper"}

user = input("Enter the character : ")
if (user not in keywords):
     print("Kindly enter valid keywords (r/p/s)")
     exit()

computer = random.choice(list(keywords.keys()))
   
    # Execution of the game
print(f"you chose: {keywords[user]}")
print(f"computer chose: {keywords[computer]}")         
   
    # The code that determines the who wins the game
if (user == computer):
    print("Draw!")
elif (user == "s" and computer == "p") or \
     (user == "r" and computer == "s") or \
     (user == "p" and computer == "r"):
    print("You win!")
else:
    print("Computer wins!")

print("Thank yoy for playing the game! :) ")
        

   
    

