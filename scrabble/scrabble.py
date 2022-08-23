import random

letters_to_scores = {'A':1, 'E':1, 'I':1, 'O':1, 'R':1, 'T':1, 'L':1, 'S':1, 'U':1,
                    'D':2, 'G':2,  'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10 }

letters_in_bag = 'E'*12 + 'A'*9 + 'I'*9 + 'O'*8 + 'N'*6 + 'R'*6 + 'T'*6 + 'L'*4 + 'S'*4 + 'U'*4 + 'D'*4 + 'G'*3 + 'B'*2 + 'C'*2 + 'M'*2 + 'P'*2 + 'F'*2 + 'H'*2 + 'V'*2 + 'W'*2 + 'Y'*2
letters_in_bag = [*letters_in_bag]

def calculate_score(word):
    total_score = 0
    for letter in word:
        total_score += letters_to_scores[letter]
    return total_score

#print(calculate_score('JACK'))

def assign_rack():
    player_rack = []
    for i in range(7):
        letter = random.choice(letters_in_bag)
        player_rack.append(letter)
        letters_in_bag.pop(letters_in_bag.index(letter))
    return player_rack, letters_in_bag