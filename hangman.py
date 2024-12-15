import random
import requests

def select_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    word = response.json()[0]
    return word

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def hangman():
    word = select_random_word()
    word_letters = set(word)
    guessed_letters = set()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    tries = 6

    print("Welcome to the Hangman Game!")
    print(display_hangman(tries))
    print("Word: " + "_ " * len(word))

    while len(word_letters) > 0 and tries > 0:
        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                tries -= 1
                print(f"Wrong guess. You have {tries} tries left.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            print("Invalid letter. Please enter a letter from a-z.")

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(display_hangman(tries))
        print("Word: " + " ".join(word_display))

    if tries == 0:
        print("You lost! The word was " + word)
    else:
        print("Congratulations! You guessed the word " + word + "!")

hangman()
