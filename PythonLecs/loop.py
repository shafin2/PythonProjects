n=18
i=0
print("You have 5 Turns Guess the number \n")
while (i<5):
    i = i+1
    print("Enter the number")
    val = int(input())
    if (val > n):
        print("Your number is greater")
        print("try again! you have",5-i,"turns left")
        continue
    elif (val < n):
        print("Your number is smaller")
        print("try again! you have",5-i," turns left")
        continue
    else:
        break

if(val==n):
    print("\nYou win! Congratulation \n you guess in",i,"turns")
else:
    print("\nyou lose")