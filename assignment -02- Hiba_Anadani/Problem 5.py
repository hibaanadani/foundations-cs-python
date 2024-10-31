def checkPassword(str):
    if len(str) < 8:
        return ("Weak Password")
    for i in str:
        if i == "!" or i =="?" or i=="$" or i=="#" and 1 <= i <= 9 and 'A' <= i <= 'Z':
            return ("Strong Password")
    else:
        return ("Weak Password")

str=input("Input: ")
print("Output: ", checkPassword(str))
