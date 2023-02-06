# Problem Statement:-
# Generate a random integer from a to b.
# You and your friend have to guess a number between two numbers,
# a and b. a and b are inputs taken from the user.
# Your friend is player 1 and plays first.
# He will have to keep choosing the number,
# and your program must tell whether the number
# is greater than the actual number or less than the actual number.
# Log the number of trials it took your friend to arrive at the number.
# You play the same game, and then the person with the minimum number of trials wins!
# Randomly generate a number after taking a and b as input and don’t show that to the user.
# Input:
# Enter the value of a
# 4
# Enter the value of b
# 13
# Output:
# Player1 :
# Please guess the number between 4 and 13
# 5
# Wrong guess a greater number again
# 8
# Wrong guess a smaller number again
# 6
# Correct, you took 3 trials to guess the number
# Player 2:
# Correct, you took 7 trials to guess the number
# Player 1 wins!






import random
class game:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.player1=0
        self.no_of_guess=0
    def turn(self) :
        print(f"So,{self.name} give your guess")
        while(True):
            player_guess=int(input("Enter the guess \n"))
            self.no_of_guess=self.no_of_guess+1
            if player_guess==self.num:
                break
            elif player_guess>self.num:
                print("You are guessing high")
                continue
            else:
                print("You are guessing low")
                continue
        print(f"{self.name} guess the number in {self.no_of_guess} turns")
    def player_1_turns(self):
        return self.no_of_guess
    def player_2_turns(self):
        return self.no_of_guess
print("First declare the range")
a = int(input("Enter minimum num\n"))
b = int(input("Enter maximum num\n"))
num = random.randint(a, b)
player1 = game("Player1", num)
player1.turn()
player_1_turns=player1.player_1_turns()
print("Now Player 2 turn")
num = random.randint(a, b)
player2 = game("Player2", num)
player2.turn()
player_2_turns=player2.player_2_turns()
if player_1_turns>player_2_turns:
    print("\nPlayer 2 win the match")
elif player_1_turns<player_2_turns:
    print("\nPlayer 1 win the match")
else:
    print("\nIts draw")







