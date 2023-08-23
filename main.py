import random
import json

def load_word_list(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

def draw_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """
    ]
    print(stages[6 - attempts])

def hangman():
    word_data = load_word_list("words.json")
    categories = list(word_data.keys())
    chosen_category = random.choice(categories)
    chosen_word = random.choice(word_data[chosen_category])
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        # Display the partially guessed word with underscores for missing letters
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "#"

        if attempts <= 3 or attempts == 6:
            # The Hint is shown at the beginning, then shows up again if the player's attempts drop down to 3
            print("Hint - Your category is :", chosen_category)
        print("Current word:", display_word)

        if display_word == chosen_word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Correct guess!")
        else:
            attempts -= 1
            draw_hangman(attempts)
            print("Wrong guess! You have", attempts, "attempts left.")

    if attempts == 0:
        draw_hangman(attempts)
        print("You lost! The word was:", chosen_word)

hangman()