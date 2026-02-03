import random
import datetime
import json
a = None
h = None
l = [1,2,3]
print("Previous score :")
try:
    with open("score.json", "r") as f:
        e = json.load(f)
        print(e)
except FileNotFoundError:
    e = {}
n = input("Do you want to start the game?\nReply with Y/N : ")

e = dict(e)
# e = {
#     str : int
# }
if n.lower() == "y":  
        x1 = datetime.datetime.now()
        print(f'The game started at {x1.strftime("%d")},{x1.strftime("%B")} and {x1.strftime("%X")}')

        name = input("Enter your name : ")
        d = {"Computer" : 0, f"{name}" : 0}

        def game_run(comp):
    
            if a == comp :
                d["Computer"] += 1
                d[f"{name}"] += 1
                return f"Your opponent chose {comp} DRAW"
            elif a == 1 and comp == 2 :
                d["Computer"] += 1
                return f"Your opponent chose {comp}.Paper YOU LOSE"
            elif a == 1 and comp == 3:
                d[f"{name}"] += 1
                return f"Your opponent chose {comp}.Scissors YOU WIN!"
            elif a == 2 and comp == 1:
                d[f"{name}"] += 1
                return f"You opponent chose {comp}.Rock YOU WIN!"
            elif a == 2 and comp == 3:
                d["Computer"] += 1
                return f"Your opponent chose {comp}.Scissors YOU LOSE!"
            elif a == 3 and comp == 1:
                d["Computer"] += 1
                return f"Your opponent chose {comp}.Rock YOU LOSE!"
            elif a == 3 and comp == 2:
                d[f"{name}"] += 1
                return f"Your opponent chose {comp}.Paper YOU WIN!"
        
        try:
            h = int(input("Enter how many times do you want to play? : "))
        except(ValueError):
            while(type(h) != int or h < 0):
                try:
                    h = int(input("Enter how many times do you want to play? : "))
                except (ValueError):
                    print(end="")
        else:
            while h < 0 :
                try:  
                    h = int(input("Enter a valid number of rounds : "))
                except (ValueError):
                    print(end="")
        
        for i in range (h):
            comp = random.choice(l)
            try:
                a = int(input("1. Rock\n2. Paper\n3. Scissors\nEnter your choice from above given choices : "))
            except (ValueError):
                    while (type(a) != int or (a not in l)):
                        try:
                            a = int(input("Enter valid choice : "))
                        except (ValueError):
                            print(end="")
            else:
                while (a not in l):
                    try:
                        a = int(input("Enter valid choice : "))
                    except (ValueError):
                        print(end="")
            print(game_run(comp))    

        print(f"The points of {name} is {d[name]}")
        print(f"The points of Computer is {d['Computer']}" )
        if  (d["Computer"] > d[f"{name}"]):
            print("You LOST!!! Hehe")

        elif (d["Computer"] < d[f"{name}"]):
            print("You WON!!! Congrats.")

        x2 = datetime.datetime.now()
        print(f'The game ended at {x2.strftime("%d")},{x2.strftime("%B")} and {x2.strftime("%X")}')
        x = x2 - x1
        x = x - datetime.timedelta(microseconds=x.microseconds)
        print(f"The game ended in {x}")

        e = e | d
        with open("score.json","w") as f:
            json.dump(e,f,indent=4)

elif n.lower() == "n" :
    print("Game is closed.")

else:
    print("Invalid Input. ")
