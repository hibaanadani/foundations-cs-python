def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        i+=1
    return fact


n= int(input("Input: "))
while(n<=0):
    print("Please enter a positive integer")
    n = int(input("Input: "))
print("Output: ", Factorial(n))
