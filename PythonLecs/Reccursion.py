

def recursive(n):
    if n==1:
        return 1
    else:
        return n * recursive(n-1)

print("enter")
number=int(input())
a=recursive(number)
print("number is",a)


