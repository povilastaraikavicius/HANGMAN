import random
from words import word_list


def choose_word(word_list):
    random_word = random.choice(word_list)
    return random_word.upper()


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def display_full_word(word):
    return word


def hangman():
    word = choose_word(word_list)
    guessed_letters = []
    attempts = 10
    lives = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 10 attempts and 6 lives.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter or the entire word: ").upper()

        if guess == word:
            print(
                f"Congratulations! You've guessed the word: {display_full_word(word)}!"
            )
            break
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            guessed_letters.append(guess)
            if guess not in word:
                lives -= 1
                print(f"Incorrect! You have {lives} lives left.")
                if lives == 0:
                    print(
                        f"Sorry, you are out of lives! The word was {display_full_word(word)}."
                    )
                    break
            else:
                print("Correct guess!")

            attempts -= 1
            print(
                f"You have {attempts} attempts and {lives} lives left. You have used these letters: {' '.join(guessed_letters)}"
            )
            if attempts == 0:
                print(
                    f"Sorry, you are out of attempts! The word was {display_full_word(word)}."
                )
                break

            if "_" not in display_word(word, guessed_letters):
                print(
                    f"Congratulations! You guessed the word: {display_full_word(word)}!"
                )
                break
        else:
            print("Please enter a single letter or the entire word.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")


hangman()
