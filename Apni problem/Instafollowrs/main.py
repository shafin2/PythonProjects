f1=open("following.txt","r")
s1=f1.read()
a1=s1.split("\n")
print(len(a1))
f2=open("followers.txt","r")
s2=f2.read()
a2=s2.split("\n")
print(len(a2))
# a1.sort()
# a2.sort()
b=0
for i1 in range(len(a1)):
    for i2 in range(len(a2)):
        if a1[i1]==a2[i2]:
            break
    else:
        print(a1[i1])
        b=b+1

print(b)



