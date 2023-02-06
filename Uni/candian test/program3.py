import re
eq=input("Enter the equation")
change=0
for char in eq:
    if (char == '+' or char == '-'):
        sign=char
        break
for char in eq:
    if(char == '+' or char=='-'):
        if(sign!=char):
            change=change+1
        sign=char

print(f"There are {change} times sign change")
eq=" " + eq
coefficient = re.findall(r' [0-9]', eq)
coefficient.sort()
largenmbr=int(coefficient[-1])
smallnumber=int(coefficient[0])
bound=abs(largenmbr/smallnumber)+1
print("Bound : ",bound)



# 2*x**4 + 4*x**8 - 9 + 3*x**5

