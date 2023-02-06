import math
def Calculate(a,n,p):
    return  int((math.pow(a,math.factorial(n)))%p)

testCase=int(input("Enter number of test case : "))
results=[]
for i in range(testCase):
    print("Enter data of case "+str(i+1))
    A=int(input("Enter A : "))
    N = int(input("Enter N : "))
    P = int(input("Enter P : "))
    results.append(Calculate(A,N,P))

print("Results")
for i in range(len(results)):
    print("Case "+str(i+1)+": "+str(results[i]))