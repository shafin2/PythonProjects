print("Firsty make your list")
print("So,how many items are there in your list?")
no_of_items = input()
lst = []
for i in range(int(no_of_items)):
    print(f"Enter your item no {i+1}")
    list_items = input()
    lst.append(list_items)
print(f"Your list is {lst}")
pllist=[]
for num in lst:
    num=int(num)
    num = num + 1
    while (True):
        b = str(num)[::-1]
        if num == int(b):
            pllist.append(num)
            break
        num = num + 1

print(f"Your palindromed list is {pllist}")

