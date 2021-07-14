# The program below breaks if anything but a number is entered.
# Try/Except blocks allow the program to deal with things that would break it
# if it were deployed.

#number = int(input("Enter a number: "))
#print(number)

try:
    # print(5/0)
    number = int(input("Enter an integer: "))
    print(number)
except ValueError:                 # Best practice is to except for specific errors
    print("Invalid input")
except ZeroDivisionError:
    print("Divide by zero")

# Can also use the following to print out the type of error you're encountering:
# EG
# except ZeroDivisionError as err:
#   print(err)