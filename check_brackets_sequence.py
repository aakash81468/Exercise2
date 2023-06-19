def check_brackets_sequence(string):
    stack = []
    opening_brackets = {'(', '[', '{', '<'}
    closing_brackets = {')', ']', '}', '>'}
    bracket_pairs = {'()', '[]', '{}', '<>'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top + char not in bracket_pairs:
                return False

    return len(stack) == 0

# Test cases
print(check_brackets_sequence("()"))  # True
print(check_brackets_sequence("([])"))  # True
print(check_brackets_sequence("{[()<>]}"))  # True
print(check_brackets_sequence("((())"))  # False
print(check_brackets_sequence("[{<>}]("))  # False
