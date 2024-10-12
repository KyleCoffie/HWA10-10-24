import math

print("Select operation:\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


def addition (num1, num2):
    return num1 + num2

def subtraction (num1,num2):
    return num1 - num2

def division (num1,num2):
    return num1/num2 

def multiplcation  (num1,num2):
    return num1 * num2


choice = input("Enter choice (1/2/3/4): ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        print(f"{num1} + {num2} = {addition(num1,num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtraction(num1,num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiplcation(num1,num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {division(num1,num2)}")
else:
    print("Invalid input. Please choose a valid operation.")