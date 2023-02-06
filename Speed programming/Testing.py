print("Enter the number")
num=int(input())
a=num
i=1
while(True):
    if a%i==0:
        a=a/i
        print(i)

    else:
        i=i+1