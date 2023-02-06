noOfCities=int(input("Enter number of cities : "))
noOfFlights=int(input("Enter number of Flights: "))
a=[]
b=[]
possibleA=[]
possibleB=[]
userA=[]
userB=[]
remainingA=possibleA
remainingB=possibleB
for i in range(noOfFlights):
    patha=int(input(f"Enter a{i+1} : "))
    pathb=int(input(f"Enter b{i+1} : "))
    a.append(patha)
    b.append(pathb)
for j in range(len(a)):
    if(a[j]>b[j]):
        userA.append(b[j])
        userB.append(a[j])
    else:
        userA.append(a[j])
        userB.append(b[j])
for i in range(1,noOfCities+1):
    for j in range(i+1,noOfCities+1):
        possibleA.append(i)
        possibleB.append(j)

for i in range(len(possibleA)):
    for j in range(len(possibleA)):
        try:
            if(userA[i]==possibleA[j] and userB[i]==possibleB[j]):
                remainingA.remove(possibleA[j])
                remainingB.remove(possibleB[j])
        except:
            pass
print(f"{len(remainingA)} more flight needed")
for  i in range(len(remainingA)):
    print(f"From {remainingA[i]} to {remainingB[i]}")