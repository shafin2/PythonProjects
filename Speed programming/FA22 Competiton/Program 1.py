def match(s,t):
    lstS = []
    lstT = []
    for a in s:
        lstS.append(a)
    for a in t:
        lstT.append(a)
    if (len(s) == len(t)):
        for i in range(len(s)):
            for i in lstS:
                for j in lstT:
                    if (i == j):
                        lstS.remove(i)
                        lstT.remove(j)
                        break
    return lstS == lstT

s=input("Enter first string : ")
t=input("Enter second string : ")
print(match(s,t))