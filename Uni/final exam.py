def get_marks(name):
    total_marks=0
    print("Marks will be out of 100")
    for i in range(4):
        while(True):
            try:
                marks=float(input(f"Enter subject-{i+1} marks : "))
                if(marks>=0 and marks<=100):
                    break
                else:
                    print("Marks will be out of 100")
                    continue
            except:
                print("Invalid input")
                continue
        total_marks=total_marks+marks
    average=total_marks/4
    grade=calculate_grade(average)
    print(f"Student {name} average marks are {average} and his grade is \"{grade}\" ")
def calculate_grade(average):
    if(average>=90 and average<=100):
        return "A"
    elif (average >= 80 and average<90):
        return "B"
    elif (average >= 70 and average<80):
        return "C"
    elif (average >= 60 and average<70):
        return "D"
    elif (average<60 and average>=0):
        return "F"

if __name__ == '__main__':
    for i in range(5):
        while(True):
            try:
                name = input(f"Enter student-{i + 1} name : ")
                break
            except:
                print("Invalid input")
                continue
        get_marks(name)