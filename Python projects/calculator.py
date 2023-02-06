print("Hello! Enter the first value")
val1=int(input())
print("Enter the operator from this +,-,*,/")
op=input()
print("Enter the second value")
val2=int(input())
if val1*val2==45*3 and op=="*":
    print("555")
elif val1+val2==56+9 and op=="+":
    print("77")
elif val1/val2==56/6 and op=="/":
    print("4")
elif op=="+":
    print("Your ans is ", val1 + val2)
elif op=="-":
    print("Your ans is ", val1 - val2)
elif op=="*":
    print("Your ans is ", val1 * val2)
elif op=="/":
    print("Your ans is ", val1 / val2)
else:
    print("You enter the Wrong operator")

