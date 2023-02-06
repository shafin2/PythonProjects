import random
i=1
computer_points=0
user_points=0
draw=0
print("Welcome to snake water gun game")
print("You have only 5 turns")
while(i<=5):
    choose={"S":"Snake","W":"Water","G":"Gun"}
    computer_side = choose["S"],choose["W"],choose["G"]
    computer_choose = random.choice(computer_side)
    print("Enter 'S' for snake, 'W' for water or 'G' for Gun")
    user_choose = input()
    user_choice = user_choose.capitalize()
    user_choice=choose[user_choice]
    print("Computer choose",computer_choose)
    if user_choice == computer_choose:
        print("Draw")
        draw=draw+1
    elif user_choice == "Snake" and computer_choose == "Water":
        print("You Win")
        user_points=user_points+1
    elif user_choice == "Snake" and computer_choose == "Gun":
        print("You loss")
        computer_points=computer_points+1
    elif user_choice == "Water" and computer_choose == "Snake":
        print("You loss")
        computer_points = computer_points + 1
    elif user_choice == "Water" and computer_choose == "Gun":
        print("You win")
        user_points = user_points + 1
    elif user_choice == "Gun" and computer_choose == "Water":
        print("You loss")
        computer_points = computer_points + 1
    elif user_choice == "Gun" and computer_choose == "Snake":
        print("You win")
        user_points = user_points + 1
    else:
        print("You entered wrong try again")
        continue
    i=i+1
game_result=f"Game results:\n"+\
            f" Your Score: {user_points} Computer Score: {computer_points} and draw: {draw}"
print(game_result)