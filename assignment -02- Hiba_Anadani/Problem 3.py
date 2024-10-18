def reverseString(str):
    reverse=""
    for i in str[::-1]:
        reverse+=i
    return reverse

str=input("Input: ")
print("Output: ", reverseString(str))


