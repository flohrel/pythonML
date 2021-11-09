import random

def result(count):
    if count == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!")
        print("You won in", count, "attempts!")
    return

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit'to end the game.")
print("Good luck!\n")
count = 0
secretNb = random.randint(1, 99)
while (1):
    print("What's your guess between 1 and 99?")
    userInput = input(">> ")
    if not userInput.isnumeric():
        if userInput == 'exit':
            print("Goddbye!")
            exit()
        else:
            print("That's not a number.")
    else:
        if int(userInput) == secretNb:
            if secretNb == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            result(count)
            exit()
        elif int(userInput) > secretNb:
            print("Too high!")
        else:
            print("Too low!")
    count += 1