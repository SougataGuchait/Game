import random 

def Game(computer , you) :
    
    if computer == you :
        return None
    
    elif computer == 'R' :
        if you == 'P' :
            return True
        elif you == 'S' :
            return False

    elif computer == 'P' :
        if you == 'S' :
            return True
        elif you == 'R' :
            return False

    elif computer == 'S' :
        if you == 'R' :
            return True
        elif you == 'P' :
            return False


print("Computer's Turn : Rock('R') , Paper('P') , Scissors('S') ? \n")
randNo = random.randint(1 , 3)

if randNo == 1 :
    computer = 'R'
elif randNo == 2 :
    computer = 'P'
elif randNo == 3 :
    computer = 'S'

you = input("Your Turn : Rock('R') , Paper('P') , Scissors('S') ? \n")

x = Game(computer , you) 

print(f"Computer Chosed {computer}\n")
print(f"You Chosed {you}\n")


if x == True :
    print("You Won.")
elif x == False :
    print("You Lose.")
elif x == None :
    print("Game Tied")