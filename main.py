import random
name = input("Enter your name : ")
d = {"Computer" : 0 , f"{name}" : 0  }
def game_run():
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
        return f"Your opponet chose {comp}.Rock YOU LOSE!"
    elif a == 3 and comp == 2:
        d[f"{name}"] += 1
        return f"Your opponent chose {comp}.Paper YOU WIN!"

l = [1,2,3]
comp = int(random.choice(l))
n = input("Do you want to start the game?\nReply with Y/N : ")
a = None
h = None
try:
    h = int(input("Enter how many times do you want to play? "))
except(ValueError):
    while(type(h) != int or h > 0):
            try:
               h = int(input("Enter how many times do you want to play? "))
            except (ValueError):
                print()
else:
    while h < 0 :
        try:  
            h = int(input("Enter a valid number of rounds"))
        except (ValueError):
                print()
if n == "Y":   
        for i in range (h):
            try:
                a = int(input("1. Rock\n2. Paper\n3. Scissors\nEnter your choice from above given choices : "))
            except (ValueError):
                    while (type(a) != int or (a < 0 or a > 3)):
                        try:
                            a = int(input("Enter valid choice : "))
                        except (ValueError):
                            print()
            else:
                while (a < 0 or a > 3):
                    try:
                        a = int(input("Enter valid choice : "))
                    except (ValueError):
                        print()
            print(game_run())
      
elif n == "N" :
    print("Game is closed.")
else:
    print("Invalid Input. ")
print(d)
if  (d["Computer"] > d[f"{name}"]):
    print("You LOST!!! Hehe")
elif (d["Computer"] < d[f"{name}"]):
    print("You WON!!! Congrats.")