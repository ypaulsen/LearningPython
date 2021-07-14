open("food_choice.txt", "r")
# "r" = read, could also specify "w" = write to modify the file.
# "a" = append - can only append
# "r+" = read and write

# The file path is unnecessary since the .txt is in the same directory
food_choice_file = open("food_choice.txt", "r+")
print(food_choice_file.readable())
print(food_choice_file.read())
# print(food_choice_file.readlines())        # This organizes it into an array
# After the file is opened it must also be closed once it's done being read.
food_choice_file.close()
# print(food_choice_file.readable())         # Throws an error here because the file is closed


