import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice():
    dice = random.randint(1,6)
    print(Fore.CYAN + "The dice shows:", dice)
    return dice

from colorama import init, Fore, Style
init(autoreset=True)

def gameon():
    pos = 1
    while True:
        if pos < 100:
            choice = input("Do you want to roll? ")
            clear_screen()
            dice = roll_dice()
            pos += dice

            if pos in snakes:
                print(Fore.RED + f"Oh no! You landed on a snake! Going back to {snakes[pos]}.")
                pos = snakes[pos]
            elif pos in ladders:
                print(Fore.GREEN + f"Oh nice! You found a ladder! Climbing up to {ladders[pos]}.")
                pos = ladders[pos]

            if pos < 100:
                print("Your Position:", pos)
        elif pos > 100:
            pos -= dice
            print("Roll too high! Stay at position:", pos)
        else:
            print(Fore.YELLOW + Style.BRIGHT + "Congratulations, you won!")
            break

# Snakes and Ladders
snakes = {99: 15, 90: 52, 74: 46, 47: 29, 27: 6, 21: 2}
ladders = {23: 42, 32: 51, 61: 79, 65: 84, 75: 94}

# Game Start
input("You need a 6 to start the game\nPress Enter to roll...")
while True:
    dice = roll_dice()
    if dice == 6:
        clear_screen()  # <--- Clear screen when game begins
        print("You rolled a 6! The game starts now.")
        gameon()
        break
    else:
        input("Not a 6, press Enter to try again...")
