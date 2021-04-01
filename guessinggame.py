secret_word = "Chimichangas"
guess = ""
guess_count = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses) : 
    if guess_count < 3:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess == secret_word:
    print("You win!")
else:
    print("Out of guesses. Try again.")