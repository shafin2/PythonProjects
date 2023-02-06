# a='2'
# b=3.4
# print(int(a)+b)
# c=['This', 'is', 'fazool', 'si', 'string', 'tou', 'khair']
#
# print(c[2])


print ("The Prime Numbers in the range are: ")
for number in range (1, 200 + 1):
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)