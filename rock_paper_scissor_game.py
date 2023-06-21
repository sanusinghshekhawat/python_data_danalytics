import random
def gamewin(cpu,player):
    if cpu==player:
        return None
    
    if cpu == "r":
        if player == "p":
            return True
        elif player == "s":
            return False
        
    if cpu == "p":
        if player == "s":
            return True
        elif player == "r":
            return False
    
    if cpu == "s":
        if player == "r":
            return True
        elif player == "p":
            return False        


print("CPU's turn: Rock(r) Paper(p) Scissor(s)?")
randNo = random.randint(1,3)
if randNo == 1 :
    cpu = "r"
elif randNo == 2 :
    cpu = "p"
elif randNo == 3 :
    cpu = "s"
player = input("Your turn: Rock(r) Paper(p) Scissor(s)?")
outcome = gamewin(cpu,player)

print("CPU chooses:" +str(cpu))
print("You choose:" +str(player))
if outcome==None:
    print("The game is a tie!")
elif outcome == True:
    print("You Win!")
else:
    print("You lose!")        
