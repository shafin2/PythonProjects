# #Pattern printing
print("Enter the number of rows you want to print")
n=int(input())
print("Enter 1 for true or 0 for false")
blval=int(input())
blval=bool(blval)
if blval==True:
    j = 1
    while (j <= n + 1):
        i = 1
        while (i < j):
            print("T", end="")
            i = i + 1
        print(" ")
        j = j + 1
elif blval==False:
    i = 1
    while (i < n+1):
        j = i
        while (j < n+1):
            print("F", end="")
            j = j + 1
        print(" ")
        i = i + 1
else:
    print("You Did not enter correct value for true/false")


