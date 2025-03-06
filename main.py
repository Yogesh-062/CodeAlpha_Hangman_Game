import random

def get_random_word():
    ranWords = ['Python', 'Programming', 'algorithm','developer']
    words = [word.lower() for word in ranWords]

    return random.choice(words)

def display_hangman(attempts):
    stages = [
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """
]
    return stages[attempts]

def play_hangman():
    word = get_random_word()
    word_display = ['_'] * len(word)
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and '_' in word_display:
        print(display_hangman(attempts))
        print("Word: ", ' '.join(word_display))
        print("Guessed letters: ", ', '.join(guessed_letters))
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
    
    if '_' not in word_display:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print(display_hangman(attempts))
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    play_hangman()