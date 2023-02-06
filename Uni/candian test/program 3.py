import string
import random



def generate_pswrd(commonletters):
    pswrd = []
    alphabets = list(string.ascii_letters)
    for i in range(length):
        pswrd.append(random.choice(alphabets))
    for letter in commonletters:
        pswrd.append(letter)
    print("".join(pswrd))

def commoncharacter(characters):
    commonletter = set.intersection(*map(set, characters))
    generate_pswrd(commonletter)

def favourit_characters():
    character=[]
    print("Enter Three Movie character")
    for i in range(3):
        while(True):
            print(f"Enter {i+1} favourite movie character ")
            user_input=input()
            for letter in user_input:
                if(letter.isdigit()):
                    print("digit not allowed. Try again")
                    break
                continue
            else:
                character.append(user_input)
                break
    commoncharacter(character)


while(True):
    print("Enter the length of password")
    length=int(input())
    if(length>=12):
        break
    else:
        print("Minimum length should be 12 . Try again")

favourit_characters()
