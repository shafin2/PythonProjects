

# Wrong try Big logical error!!!!!!!!!!!

import random
no_of_friends=input("Enter the number of friends\n")
friends_names=[]
for i in range(1,int(no_of_friends)+1):
    print(f"Enter name of friend {i}  ")
    friend_name=input()
    single_name=friend_name.split(" ")
    for name in single_name:
        friends_names.append(name)

first_index=0

for b in range(int(len(friends_names)/2)):
    a=random.randint(b+1, int(len(friends_names)-1))
    if a%2==0 or a==0:
        if a+2 < len(friends_names):
            print(f"Jambled name is {friends_names[first_index]} {friends_names[a+2]}")
            first_index = first_index + 2
        else:
            print(f"Jambled name is {friends_names[first_index]} {friends_names[a-1]}")
            first_index = first_index + 2
    else:
        if a+2>len(friends_names):
            print(f"Jambled name is {friends_names[first_index]} {friends_names[a]}")
            first_index=first_index+2
        elif a+2==len(friends_names)-1:
            print(f"Jambled name is {friends_names[first_index]} {friends_names[a-1]}")
            first_index = first_index + 2
        else:
            print(f"Jambled name is {friends_names[first_index]} {friends_names[a + 2]}")
            first_index = first_index + 2



# import random
# t = int(input("Enter the number of names you want to input\n"))
# names = []
# for i in range(t):
#     names.append(list(input().split(" ")))
# for i in range(t):
#     print(names[i][0] + " " + names[random.randint(i, t-1)][random.randint(1, len(names[i])-1)])