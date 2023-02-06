# import math as m
# import random
#
# # value='''
# #                                                                   Welcome to python
# # '''
# # print(value)
#
# # # # Data
# # # # name
# # # print("Name : Shafin-uz-zaman\n")
# # # # dob
# # # print("DOB : 4 dec 2003\n")
# # # # reg no
# # # print("Reg no : SP22-BCS-063")
# # #
# # # print("hello");print("world")
# # # number1=50
# # # number2=75.5
# # # number3=number2*2
# # # print
# #
# # a="Zaman"
# # print("Shafin",a)
#
#
# # id=input("Enter your ID : ")
# # name=input("Enter your name : ")
# # gpa=input("Enter your gpa : ")
# # cgpa=input("Enter your cgpa : ")
# # section=input("Enter your section : ")
# # gender=bool(input("Enter your gender : "))
# #
# # print(f"Student with ID {id} and Name {name} has CGPA {cgpa}. Gender is {gender}\nHe/She enrolled in section {section}")
#
# #
# # n1=int(input("Enter first number : "))
# # n2=int(input("Enter first number : "))
# # print(f"{str(n1)+str(n2)}")
#
# #
# # value1="abcdjksjdik sjdklsmmdiksd"
# # # print(value1[0:])
# # message="This is the"
# # r=-2.9
# # number=3.1
# # print(message.replace("the","ag"))
# # print(round(r))
# # print(abs(r))
# # print(m.ceil(number))
#
# # i=1
# # while(i<=40):
# #     if(i%4==0 and i%2==0):
# #             print(i)
# #
# #
# #     i=i+1
#
# #
# # i=random.randint(1,10)
# # j=0
# # while(j<3):
# #     print("Enter number ");
# #     number=int(input())
# #     if(number==i):
# #         print("You win")
# #         break
# #     j=j+1
# # else:
# #     print("Try again")
#
# # for i in range(3):
# #     for j in range(4):
# #         print(f"{i},{j}")
#
# # numbers = (5, 6, 2, 3, 4, 2)
# #
# # print(numbers)
# #
# # # user = int(input("Enter a number: "))
# # #It insets a number after the given index e.g insert(1, 10)
# # #It will insert the 10 after index 1
# # numbers.sort()
# # print(numbers)
#
# #
# # a=10
# # print(f"variable value is {a}")
# def marks(marking_type,no_of_marking,average_in_total):
#     average=0
#     average_in_total=(average_in_total/no_of_marking)/100
#     print(average_in_total)
#     for i in range(no_of_marking):
#         print(f"Enter total marks of {marking_type}-{i+1} ")
#         total_marks=int(input())
#         print(f"Enter obtain marks of {marking_type}-{i+1} ")
#         obtain_marks = int(input())
#         weightage=((obtain_marks/total_marks)*100)*average_in_total
#         print(weightage)
#         average=average+weightage
#     return average
# if __name__ == '__main__':
#     course="Ict"
#     print(marks(f"quiz of {course}",3,15))

course_gpa=["3.0 is GPA and Grade is B","3.3 is GPA and Grade is B+"]

total_gpa=0
for i in range(len(course_gpa)):
    lst=course_gpa[i].split(" ")
    total_gpa=total_gpa+float(lst[0])
print(total_gpa)