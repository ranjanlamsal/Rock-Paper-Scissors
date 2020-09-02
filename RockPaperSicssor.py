import random
comp_points = 0
usr_points = 0
print('''Welcome Rock Paper Scissor game.
 You have to type 'p' for paper,
 's' for Scissor and 'r' for rock.
 There will be total of 10 rounds and results will be displayed.
 Type "exit" if you want to terminate the game\v''')
li = ["r", "p", "s"]
i = 0
while True:
    while i < 10:
        usr_choice = input("'p' or 's' or 'r' ?\n>>").lower()
        rand = random.choice(li)
        if usr_choice in li or "exit":
            # global comp_points
            # global usr_points
            if usr_choice == rand:
                print(f"Draw.\t\t{9-i} rounds left\n")
                i = i + 1
            elif usr_choice == "r" and rand == "p":
                print(f"Computer +1 point.\t\t{9-i} rounds left\n")
                i = i + 1
                comp_points = comp_points + 1
            elif usr_choice == "r" and rand == "s":
                print(f"User +1 point.\t\t{9-i} rounds left\n")
                i = i + 1
                usr_points = usr_points + 1
            elif usr_choice == "p" and rand == "r":
                print(f"User +1 point.\t\t{9-i} rounds left\n")
                i = i + 1
                usr_points = usr_points + 1
            elif usr_choice == "p" and rand == "s":
                print(f"Computer +1 point.\t\t{9-i} rounds left\n")
                i = i + 1
                comp_points = comp_points + 1
            elif usr_choice == "s" and rand == "p":
                print(f"User +1 point.\t\t{9-i} rounds left\n")
                i = i + 1
                usr_points = usr_points + 1
            elif usr_choice == "s" and rand == "r":
                print(f"Computer +1 point\t\t{9 - i} rounds left\n")
                i = i + 1
                comp_points = comp_points + 1
            else:
                break
        else:
            print('''no command exist. You have to type 'p' for paper,
                's' for Scissor and 'r' for rock. To terminate type 'exit'.''')
            continue
    print("Game Completed.")
    if usr_points > comp_points:
        print(f"Congratulation you won\n Your point: {usr_points}\nComputer points:{comp_points}")
    elif usr_points == comp_points:
        print(f"Game Draw!\nYour point: {usr_points}\nComputer points:{comp_points}")
    else:
        print(f"Sorry you lose.\nYour point: {usr_points}\nComputer points:{comp_points}")
    conti = input("Do you want to continue?('y' for yes)").lower()
    if conti == "y":
        continue
    else:
        break
