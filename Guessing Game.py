# A guessing game

# Set parameters
secret_word = "telescope"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# while loop checks conditions
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("What is your guess?")
        guess_count += 1
    else:
        out_of_guesses = True

# only two ways out of the while loop:
if out_of_guesses:
    print("Out of Guesses!")
else:
    print("Winner!")