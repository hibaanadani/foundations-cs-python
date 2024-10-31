def Divisor(n):
    div = []
    for i in range(1,n+1):
        if(n%i==0):
            div.append(i)
            i+=1
        else:
            i+=1
    return div


n= int(input("Input: "))
while(n<=0):
    print("Please enter a positive integer")
    n = int(input("Input: "))

print("Output: ", Divisor(n))