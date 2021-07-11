name = input("Enter your name:")
age = input("Enter your age:")
print("Hello " + name + "! You are " + age)

# Building a calculator

num1 = input("Enter a number:")
num2 = input("Enter a number:")
result = num1 + num2 # Doesn't work because Python converts to string
print(result)

num1 = input("Enter a number:")
num2 = input("Enter a number:")
result = float(num1) + float(num2) # float() or int() converts to numeric (int requires integer)
print(result)


