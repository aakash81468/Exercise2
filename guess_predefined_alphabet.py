class SmallerAlphabetException(Exception):
    pass

class GreaterAlphabetException(Exception):
    pass

def guess_alphabet(predefined_alphabet):
    user_guess = input("Guess the alphabet: ")

    if user_guess < predefined_alphabet:
        raise SmallerAlphabetException("Entered alphabet is smaller than the predefined alphabet")
    elif user_guess > predefined_alphabet:
        raise GreaterAlphabetException("Entered alphabet is greater than the predefined alphabet")
    else:
        print("Congratulations! You guessed the correct alphabet.")

# Predefined alphabet
predefined_alphabet = 'F'

try:
    guess_alphabet(predefined_alphabet)
except SmallerAlphabetException as e:
    print("Error:", str(e))
except GreaterAlphabetException as e:
    print("Error:", str(e))
