import random
from random import choice

from extras.hangman_art import logo,stages
from extras.hangman_words import word_list



def check_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print("You've already guessed that letter!")
        else:
            return guess




def hangman():
    lives = 6
    chosen_word = random.choice(word_list)
    guessed_letters = []
    display = [letter if letter == guessed_letters else "_" for letter in chosen_word]

    print(f"{logo}\nGame Started....")


    print(chosen_word)
    while lives > 0:
        print(display)
        user_guess = check_valid_guess(guessed_letters)
        if user_guess not in chosen_word:
            lives -= 1
            print(f"You've guessed {user_guess}, which is not in the word. You lose a life.\nYou've {lives} attempts left.")
            print(stages[lives])
            if lives == 0:
                print(f"Game over! The word was '{chosen_word}'.")
                break
        else:
            # guessed_letters.insert()
            print("Good Guess.")


def play_again():
    while True:
        choice = input("Do you want to play again? ['Yes','No']").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    while True:
        hangman()
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break
