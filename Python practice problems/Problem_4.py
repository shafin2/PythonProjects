# The task you have to perform is “The Next Palindrome.” This task consists of a total of 15 points to evaluate your performance.
# Problem Statement:-
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
# 676, 616, mom, 100001.
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
# Input:
# 3
# 451
# 10
# 2133
# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2311 is 2222
# These tasks will improve your logic-making skills and logic is the basics of programming.
no_of_cases=input("How many numbers do you want to enter?\n")
for a in range(int(no_of_cases)):
    num = int(input(f"Enter the number {a+1}\n"))
    num = num + 1
    while (True):
        b = str(num)[::-1]
        if num == int(b):
            print("The next palindrome of your number is",num)
            break
        num = num + 1
