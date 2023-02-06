#Problem link:
# https://codeforces.com/blog/entry/82143

print("Enter the number of inputs : ")
no_of_input=int(input())
problem_ans=0
for i in range(1,no_of_input+1):
    print("Enter ",i," input")
    user_input=input()
    a=user_input.split()
    if(a[0]=='0' and a[1]=='0'):
        continue
    elif (a[0] == '0' and a[2] == '0'):
        continue
    elif (a[1] == '0' and a[2] == '0'):
        continue
    else:
        problem_ans=problem_ans+1

print("They will ans ",problem_ans," problems")