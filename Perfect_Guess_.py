import random

ran = random.randint(1, 100)
num = -1
guesses = 1

while(num != ran):
    guesses += 1
    num = int(input("Enter the number : "))
    print(num)

    if(num > ran):
        print("Bit lower than that")

    else:
        print("Bit higher than that")

    
print(f"Congragulations you have guessed the nummber {num} in {guesses -1} attempts.") 




