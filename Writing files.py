# Create a new file
food_choice_file2 = open("food_choice2.txt", "w")
food_choice_file2.write("3.78 F")
food_choice_file2.close()
# the new file has one entry

# Append to an existing file:
food_choice_file2 = open("food_choice2.txt", "a")
food_choice_file2.write("\n2.78 M")          # The escape character (\n) tells python to put the hew data on a new line
food_choice_file2.close()

food_choice_file2 = open("food_choice2.txt", "r")
print(food_choice_file2.read())
food_choice_file2.close()