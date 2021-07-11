# Function to say hello
# is a Keyword tells python we're creating a function
def say_hi():
    print("Hello user")

# to call function:
say_hi()


# To require parameters:
def say_hi2(name):
    print("Hello " + name)

say_hi2("Yale")
say_hi2("Steve")

# return statement
def cube(num):
    return num*num*num

print(cube(3))

result = cube(4)
print(result)



