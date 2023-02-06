def calculate_bill(unit):
    if(unit>0 and unit<100):
        price=9.5
    elif(unit>100 and unit<200):
        price=14.5
    else:
        price = 20.5
    return price*unit+1000
if __name__ == '__main__':
    print("Welcome to bill calculator")
    for i in range(4):
        while(True):
            try:
                print("Enter department name : ")
                department_name = input()
                break
            except:
                print("Wrong input")
                continue
        while(True):
            try:
                print("Enter units : ")
                units = int(input())
                if(units>=0):
                    break
                else:
                    print("Units can not be negative number")
            except:
                print("Wrong input")
                continue
        result=calculate_bill(units)
        print(f"Total bill of {department_name} is {result} ")











