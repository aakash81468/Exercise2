import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach"]

def get_anagram(word):
    # Randomly shuffle the letters of the word
    anagram = list(word)
    random.shuffle(anagram)
    return ''.join(anagram)

def play_game():
    # Select a random word from the list
    word = random.choice(words)
    attempts = 5

    # Generate the anagram
    anagram = get_anagram(word)

    print("Welcome to the Anagram Game!")
    print("Unscramble the given word within a limited number of attempts.\n")

    while attempts > 0:
        print("Attempts left:", attempts)
        print("Anagram:", anagram)

        guess = input("Enter your guess (or type 'hint' for a clue): ").lower()

        if guess == "quit":
            print("Quitting the game...")
            return

        if guess == word:
            print("Congratulations! You guessed the word correctly!")
            return

        if guess == "hint":
            print("Clue: The word is a type of fruit.")
            attempts -= 1
            continue

        print("Incorrect guess!")
        attempts -= 1

    print("Out of attempts. The word was:", word)

# Start the game
play_game()
