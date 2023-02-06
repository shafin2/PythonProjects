print("Enter the string")
str=input()
a=str.split("(")
b=a[1].split(")")
c=b[0]
print(type(c))
c.split()
lst=[]
for i in range(len(c)):
    lst.append(c[i])
lst.reverse()
str1=""
str1 += a[0]
for j in lst:
    str1 += j
str1 += b[1]
print("solution(inputstring) = " , str1)
