import sys

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
DEFAULT_HAND_SIZE = 7
BONUS_PTS = 50
DEFAULT_GAME_TIME = 120 # in sec

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

HAND_SIZE = DEFAULT_HAND_SIZE
DEFAULT_TIME = DEFAULT_GAME_TIME

if __name__ == '__main__':
    while True:
        question = input("What do you want to change?\n"
                         "Hand size? - press h\n"
                         "Default time? - press d\n"
                         "Exit - press e\n")

        if question == 'h':
            TRY_HAND_SIZE = int(input("Enter the number from 4 to 15: "))
            if 4 <= TRY_HAND_SIZE <= 15:
                HAND_SIZE = TRY_HAND_SIZE
            else:
                print("Invalid input. Please, try again.")
        elif question == 'd':
            TRY_DEFAULT_TIME = int(input("Enter the number from 10 to 600: "))
            if 10 <= TRY_DEFAULT_TIME <= 600:
                DEFAULT_TIME = TRY_DEFAULT_TIME
            else:
                print("Invalid input. Please, try again.")
        elif question == 'e':
            break
        else:
            print("Invalid input. Please, try again.")

    with open('../data/game_settings.txt', 'w') as f:
        print('HAND_SIZE = ' + str(HAND_SIZE) + '\nDEFAULT_TIME = ' + str(DEFAULT_TIME), file=f)