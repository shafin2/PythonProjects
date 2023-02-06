words_dict={}
no_of_int=0
no_of_float=0
no_of_str=0
with open("abc","r") as fl:
    for line in fl:
        for word in line.split(" "):
            for letter in word:
                if (letter == "\n"):
                    word=word[:-1]
            if word in words_dict:
                words_dict[word]=words_dict.get(word,0) + 1
            else:
                words_dict[word]=1
            if(word.isdigit()):
                no_of_int = no_of_int +1
            elif(word.replace('.', '', 1).isdigit()):
                no_of_float =no_of_float+1
            else:
                no_of_str=no_of_str+1


print("Data type : Frequency")
print("Int:",no_of_int)
print("Float:",no_of_float)
print("String:",no_of_str)
print("")

print("{:<20} {:<20}".format('Words', 'Frequency'))

for key, value in words_dict.items():
    print("{:<20} {:<20}".format(key, value))