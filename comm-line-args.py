# Command-line arguments program
# Run using: python3 comm-line-args.py 2 add 3

import sys

def addition(num1, num2):
    add = num1 + num2
    return add

def substract(num1, num2):
    sub = num1 - num2
    return sub

def multiply(num1, num2):
    multi = num1 * num2
    return multi

def divide(num1, num2):
    div = num2/num1
    return div

num1 = float(sys.argv[1])
operate = sys.argv[2]
num2 = float(sys.argv[3])

if operate == "add":
    output = addition(num1, num2)
    print(f"Addition is: {output}")
elif operate == "substract":
    output = substract(num1, num2)
    print(f"Substration is : {output}")
elif operate == "multiply":
    output = multiply(num1, num2)
    print(f"Multiplication is: {output}")
elif operate == "divide":
    output = divide(num1, num2)
    print(f"Division is: {output}")
else:
    print("Invalid input")
