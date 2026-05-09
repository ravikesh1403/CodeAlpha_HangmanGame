#  Hangman Game

import random

# List of words
word_list = ["apple", "tiger", "chair", "pizza", "robot"]

# Randomly choosing one word
secret_word = random.choice(word_list)

# Empty list to store guessed letters
guessed_letters = []

# Total chances
wrong_guesses = 6

print("===== Welcome to Hangman Game =====")

# Game loop
while wrong_guesses > 0:

    # Displaying word with blanks
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Checking win condition
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly.")
        break

    # Taking input from user
    user_guess = input("Enter a letter: ").lower()

    # Checking input length
    if len(user_guess) != 1:
        print("Please enter only one letter.")
        continue

    # Checking repeated letter
    if user_guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Adding guess to list
    guessed_letters.append(user_guess)

    # Checking correct or wrong guess
    if user_guess in secret_word:
        print("Correct Guess!")
    else:
        wrong_guesses -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", wrong_guesses)

# If user loses
if wrong_guesses == 0:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")
