import random

def create_substitution_table():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    substitution = {}
    for letter in letters:
        substitution[letter] = random.sample(letters, 3)
    return substitution

def substitute(text, table):
    substituted = []
    for char in text:
        if char in table:
            substituted.append(random.choice(table[char]))
        else:
            substituted.append(char)
    return ''.join(substituted)
