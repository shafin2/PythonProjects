# Problem Statement:-
# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or a few less apples.
# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.
# Input:
# Take input n, mn, and mx from the user.
# Output:
# Print whether the numbers between mn and mx are divisors of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.
# Example:
# If n is 20 and mn=2 and mx=5
# 2 is a divisor of20
# 3 is not a divisor of 20
# 5 is a divisor of 20





if __name__ == '__main__':
    while(True):
        try:
            print("Welcome! Enter th number of apples you have")
            n = int(input())
            if n > 0:
                print("Pls also enter the range of students")
                print("First, enter max range")
                mx = int(input())
                print("Second, enter min range")
                mn = int(input())
                if mn >= 0 and mx > 0:
                    if mx == mn:
                        if n % mn == 0:
                            print(f"Yes,{n} apples can be distributed in {mx} students")
                        else:
                            print(f"no,{n} apples cannot be equally distributed in {mx} students")
                        break
                    elif mx > mn:
                        for i in range(mn, mx + 1):
                            if n % i == 0:
                                print(f"Yes,{n} apples can be distributed in {i} students")
                            else:
                                print(f"no,{n} apples cannot be equally distributed in {i} students")
                        break
                    else:
                        print("You give wrong range,Try again")
                        continue
                else:
                    print("pls enter the right range,Try again")
                    continue
            else:
                print("I think you need apples,Try again")
                continue
        except:
            print("Enter integer,Try again")
            continue


