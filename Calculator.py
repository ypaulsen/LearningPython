# Building a simple calculator
num1 = float(input("Number: ")) # float immediately converts to numeric
op = input("Operator: ")
num2 = float(input("Number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Error: Invalid Operator")

