print("Enter value it return one value at once")
userinput=input()
lst=userinput.strip()
newlst=[]


for i in range(len(lst)):
    score = 0
    for j in range(0,i+1):
        if(lst[i]==lst[j]):
            score=score+1
    if(score<=1):
        newlst.append(lst[i])
newlst.sort()
for i in range(len(newlst)):
    print(newlst[i],end='')