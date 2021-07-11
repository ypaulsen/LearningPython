# If
is_male = False # Boolean variable
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or a tall male")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either female or short or both")

if is_male and is_tall:
    print("You're a tall male")
elif is_male and not(is_tall):            # elif == else if
    print("You are a Short male")
elif not(is_male) and is_tall:
    print("You are a tall woman")
else:
    print("You are a short woman")


# Comparisons in conditional programming
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return(num3)

print(max_num(3,4,5))
print(max_num(33,4,5))

