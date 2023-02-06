print("Enter the number")
num=input()
num.split()
sum=0
for i in range(len(num)):
    sum=sum+int(num[i])
cond1=sum-1
flag=0
for j in range(2,cond1):
    if cond1%j==0:
        flag=flag+1
first_half_sum=0
for k in range(int(len(num)/2)):
    first_half_sum=first_half_sum+int(num[k])
second_half_sum=0
lst=[]
for i in range(len(num)):
    lst.append(num[i])
lst.reverse()
for z in range(int(len(num)/2)):
    second_half_sum=second_half_sum+int(lst[z])
cond2=first_half_sum-second_half_sum
cond2_sum=0
for y in range(1,abs(cond2)):
    if cond2%y==0:
        cond2_sum=cond2_sum+y

#Main condition
if flag==0 and abs(cond2)==cond2_sum:
    print("Number is cold")
else:
    print("Number is hot")


