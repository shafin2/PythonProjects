# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sorts of errors like :            (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible
def age_at_100(user_input):
    user_input[0]=int(user_input[0])
    user_input[1]=int(user_input[1])
    if user_input[0] > 2022:
        print("You are not Born yet")
    elif user_input[0] < 120:
        age_now = 2022 - user_input[0]
        age_then = age_now + 100
        print(f"You will be 100 years old in {age_then}")
        age_at_year(age_now,user_input[1])
    elif user_input[0] > 1902 and user_input[0] < 2022:
        age_then = user_input[0] + 100
        print(f"You will be 100 years old in {age_then}")
        age_at_year(user_input[0],user_input[1])
    else:
        print("Haha! You seem to be the  oldest person alive")
def age_at_year(age,user_input):
            if age>user_input:
                print(f"You were not born in {user_input}")
            elif age<user_input:
                print(f"You will be {(user_input-age)} years old in {user_input}")
            else:
                print("You not use age function")

if __name__ == '__main__':
    print("Welcome! this program is designed only for alive humans")
    print("Enter your Age or Year of birth")
    print("Optional! You can also provide random year to find what your age on"
          "that particular year but pls seprate it after hypen(-) like 2000-2099")
    try:
        user_input = input()
        user_age = user_input.split("-")
        age_at_100(user_age)
    except:
        user_age=["0","0"]
        age_at_100(user_age)