import sys


def returnDigits(n):
    digit=1
    if -10<n<10:
        return digit
    else:
        return digit +returnDigits(n//10)

def returnMax(arr):
    max=0
    if arr == '':
        return max
    elif len(arr)==1:
        return arr[0]
    else:
       max= returnMax(arr[1:])
       # Recursive case: Compare the first element with the maximum in the rest of the list
       return arr[0] if arr[0] > max else max


def countTag(code, tag):
    if not code:
        return 0
    # Find the opening tag
    open_tag = f"<{tag}>"
    close_tag = f"</{tag}>"
    start_index = code.find(open_tag)
    end_index = code.find(close_tag)

    # If either the opening or closing tag is not found, return 0
    if start_index == -1 or end_index == -1:
        return 0

    # Recursively count the occurrences of the tag in the remaining HTML
    return 1 + countTag(code[end_index+len(close_tag):],tag)

x=int(input("enter a number from 1 to 4 where:1. Count Digits 2. Find Max 3. Count Tags 4. Exit"))
while 1>x or x>4:
    print("Enter a number from 1 to 4")
    x= int(input())

if x==1:
    y= int(input("Input: "))
    print("Y = " + str(y) +" has " + str(returnDigits(y)) + " digits")

if x==2:
    y=input("enter array")
    if y.strip()=="":
        print("Max number in array is " + str(returnMax(y)))
    else:
        arr = [int(n) for n in y.split(" ")]
        print("Max number in array is " + str(returnMax(arr)))



if x==3:
    code=[]
    while True:
        y = input("code: ")
        if y.lower() == "</html>":
            break
        code.append(y)
    userInput="\n".join(code)
    tag=input("tag: ")
    print("there is ", countTag(userInput,tag) , tag ,"in the code")

if x==4:
    sys.exit()