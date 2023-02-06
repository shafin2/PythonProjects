#LIST COMPREHENSION
# ls =[i for i in range(1000) if i%8==0]
# print(ls)


#DICTIONARY COMPREHENSION
#Set is also be created by curly braces but in set we do not use colon(:) to assign a value
#and difference from list is that list can reapeat the value but set cannot
#As (Set is collection of  well-defined distict objects) so one value can not be repeat
# dict2={i:f"itemo{i}" for i in range(100)}
# print(dict2)
# print(dict2[70])


#GENERATOR COMPREHENSION
#for making generator we use parenthesis()
# gn=(i for i in range(100))
# print(type(gn))

# gn=(i for i in range(2345432,13883456765456))
# print(gn.__next__())
# print(gn.__next__())
# print(gn.__next__())



#EXERCISE

print("How many input do you want:")
no_of_input=input()
print("What do you want to print?\n"
      "press 1 for list,2 for dictionary and 3 for set")
selected=input()
print("enter",no_of_input,"Numbers by press enter after each")
if selected=="1":
    user_inputs = [input() for i in range(int(no_of_input))]
    print(type(user_inputs))
    print("Your list is",user_inputs)
elif selected=="2":
    user_inputs = {i :input() for i in range(int(no_of_input))}
    print(type(user_inputs))
    print("Your Dictionay is",user_inputs)
elif selected=="3":
    user_inputs = {input() for i in range(int(no_of_input))}
    print(type(user_inputs))
    print("Your Set is",user_inputs)
else:
    print("Your Selection is wrong")


