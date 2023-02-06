course_gpa=[]
def total_marks_of_course(course_name,theory_weightage,lab_weightage,lab):
    print(f"First Enter theory marks of {course_name}")
    print(f"Enter theory Quiz marks of {course_name}")
    no_of_marking=int(input(f"How many Quiz taken in {course_name} : "))
    quiz=marks(f"{course_name} quiz",no_of_marking,15)
    print(f"Enter theory Assignment marks of {course_name}")
    no_of_marking=int(input(f"How many Assignment taken in {course_name} : "))
    assignment=marks(f"{course_name} assignment",no_of_marking,10)
    print(f"Enter theory Midterm marks of {course_name}")
    midterm = marks(f"{course_name} midterm", 1, 25)
    print(f"Enter theory Final marks of {course_name}")
    final= marks(f"{course_name} Final", 1, 50)
    theory_total=quiz+assignment+midterm+final
    if(lab==1):
        print(f"Now Enter Lab marks of {course_name}")
        print(f"Enter Lab Assignment marks of {course_name}")
        no_of_marking = int(input(f"How many Lab-Assignment taken in {course_name} : "))
        assignment = marks(f"{course_name} assignment", no_of_marking, 25)
        print(f"Enter Lab midterm marks of {course_name}")
        midterm = marks(f"{course_name} midterm", 1, 25)
        print(f"Enter Lab final marks of {course_name}")
        final = marks(f"{course_name} Final", 1, 50)
        Lab_total = assignment + midterm + final
        total_average = (theory_total * theory_weightage) + (Lab_total * lab_weightage)
    else:
        total_average=theory_total
    gpa=check_gpa(total_average)
    course_gpa.append(gpa)
    print(f"\nTotal numbers in {course_name} are {total_average}")
    print(f"And {gpa}\n\n")
def marks(marking_type,no_of_marking,average_in_total):
    average=0
    average_in_total=(average_in_total/no_of_marking)/100
    for i in range(no_of_marking):
        print(f"Enter total marks of {marking_type}-{i+1} ")
        total_marks=int(input())
        print(f"Enter obtain marks of {marking_type}-{i+1} ")
        obtain_marks = int(input())
        weightage=((obtain_marks/total_marks)*100)*average_in_total
        average=average+weightage
    return average
def check_gpa(average_marks):
    if(average_marks>=85 and average_marks<=100):
        return "4.0 is GPA and Grade is A"
    elif(average_marks>=80 and average_marks<85):
        return "3.7 is GPA and Grade is A-"
    elif(average_marks>=75 and average_marks<80):
        return "3.3 is GPA and Grade is B+"
    elif (average_marks >=70 and average_marks < 75):
        return "3.0 is GPA and Grade is B"
    elif (average_marks >= 65 and average_marks < 70):
        return "2.7 is GPA and Grade is B-"
    elif (average_marks >= 60 and average_marks < 65):
        return "2.3 is GPA and Grade is C+"
    elif (average_marks >= 55 and average_marks < 60):
        return "2.0 is GPA and Grade is C"
    elif (average_marks >= 50 and average_marks < 55):
        return "1.7 is GPA and Grade is C-"
    elif (average_marks >= 45 and average_marks < 50):
        return "1.3 is GPA and Grade is D"
    elif (average_marks >= 0 and average_marks < 45):
        return "0 is GPA and Grade is f"
    else:
        return "0"
def overall_gpa():
    total_gpa=0
    for i in range(len(course_gpa)):
        lst=course_gpa[i].split(" ")
        total_gpa=total_gpa+float(lst[0])
    return total_gpa
if __name__ == '__main__':
    print("GPA Calculator")
    no_of_courses=int(input("Enter no of courses : "))
    for i in range(no_of_courses):
        while(True):
            course_name = input(f"Enter course-{i+1} name ")
            print("Three are three type of courses given in Comsats ")
            print("1) 4 credit hour course in which 75% is for theory and 25% for lab")
            print("2) 3 credit hour course with lab in which 66.7% is for theory and 33.3% for lab")
            print("3) 3 credit hour course without lab in which 100% is for theory ")
            print("Press 1,2 and 3 for which you want to calculate Gpa ")
            user_choice = input()
            if (user_choice == '1'):
                # fun(course name,theory weightage,lab weightage,(if lab is included )?1:0)
                marks=total_marks_of_course(course_name, 0.75, 0.25, 1)
                break
            elif (user_choice == '2'):
                total_marks_of_course(course_name, 0.67, 0.33, 1)
                break
            elif (user_choice == '3'):
                total_marks_of_course(course_name, 100, 0, 0)
                break
            else:
                print("Invalid input")
                continue
    total_gpa=overall_gpa()
    total_gpa=total_gpa/no_of_courses
    print(f"\n\nYour Total GPA is {total_gpa} ")