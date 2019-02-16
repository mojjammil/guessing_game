# store secret word
secret_word = "hilarious"
# Take secret word input
guessed_word = ""
# Set guess limits
guess_limit = 5
# Count guesses
guess_count = 0
# Out of guess
out_of_guess = False

# Function for matching guess vs secret word
while guessed_word.lower() != secret_word.lower() and not(out_of_guess):
    if guess_count < guess_limit:
        guessed_word = input("What do you call a funny mountain?: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You are out luck")
else:
    print("You got it dude!")



