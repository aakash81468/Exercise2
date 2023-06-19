import re

def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False

# Example usage
regex_string = input("Enter a regex string: ")

if is_valid_regex(regex_string):
    print("Valid regex!")
else:
    print("Invalid regex!")
