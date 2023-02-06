print("Welcome Pls enter your age")
age=int(input())
if age>100 or age<7:
    print("Enter the right age")
elif age>18:
    print("you can drive")
elif age==18:
    print("we cannot decide yet")
else:
    print("you are not elligible for driving")
print("Thanks for coming")