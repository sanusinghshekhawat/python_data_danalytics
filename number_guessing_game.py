print("Number guessing game:\nBot selects a number")
import random
randNumber = random.randint(1,101)
userGuess = None
guesses = 0
while userGuess!=randNumber:
    userGuess = int(input("Enter Your Guess: "))
    guesses = guesses+1
    if userGuess==randNumber:
        pass
    elif userGuess>randNumber:
        print("Guess a lower Number!\n")
    else:
        print("Guess a higher Number!\n")
        
    
print(f"You guessed the correct number in {guesses} guesses")

with open("hiscore.txt","r") as f:
    hiscore = f.read()
with open("hiscore.txt","w") as f:
    if hiscore == "":
        f.write(str(guesses))
    elif guesses<int(hiscore):
        print(("Congrats! You have broken the Hiscore"))
        f.write(str(guesses))

        