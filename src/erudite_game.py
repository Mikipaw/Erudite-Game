import random
import re
import src.settings as settings
from threading import Timer

WORDLIST_FILENAME = "../words.txt"

def load_words_from_file():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    input_file = open(WORDLIST_FILENAME, 'r')
    word_list = []
    for line in input_file:
        word_list.append(line.strip().lower())

    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list

    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: int >= 0
    """
    result = 0
    for c in word:
        result += settings.SCRABBLE_LETTER_VALUES[c]
    result *= len(word)
    if len(word) == n: result += settings.BONUS_PTS
    return result


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")
    print()


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = settings.VOWELS[random.randrange(0, len(settings.VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = settings.CONSONANTS[random.randrange(0, len(settings.CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)

    returns: dictionary (string -> int)
    """
    chand = hand.copy()
    for letter in word:
        if letter in chand:
            chand[letter] -= 1
        if chand[letter] == 0:
            chand.pop(letter)
    return chand


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    if word not in word_list:
        return False

    chand = hand.copy()
    for i in word:
        if i in chand:
            chand[i] -= 1
            if chand[i] == -1:
                return False
        else:
            return False

    return True


def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)

    returns: integer
    """
    current_sum = 0
    for item in hand.keys():
        current_sum += hand[item]
    return current_sum


def play_hand(hand, word_list, n, single = True, dif = 'e'):
    """
    Returns sum of points for words founded.

    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * User has limited time depended of difficulty.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; required for additional points)
      single: bool (default True)
      dif: str (default 'e' means easy)

    """
    current_sum = 0

    with open('../data/game_settings.txt', 'r') as f:
        line = f.readline()
        nums = re.findall(r'\d+', line)
        settings.DEFAULT_TIME = int(nums[0])

    current_dif = ['e', 'm', 'h', 'i'].index(dif)
    timeout = settings.DEFAULT_TIME - current_dif * 30
    t = Timer(timeout, print, ['\nPress Enter to continue', ''])
    t.start()

    while not calculate_hand_len(hand) == 0:
        print("Current Hand: ", end="")
        display_hand(hand)

        word = input("Enter word, or a . to indicate that you are finished: ")
        if not t.is_alive():
            print('Your time is up.')
            t.cancel()
            if single:
                print("Game over! Total score: " + str(current_sum) + " points.")
            else:
                print("Current points: " + str(current_sum))
            return current_sum

        if word == ".":
            break

        else:
            if not is_valid_word(word, hand, word_list):
                print("Invalid word")
            else:
                current_sum += get_word_score(word, n)
                print(word + " earned " + str(get_word_score(word, n))
                      + " points. Total: " + str(current_sum) + " points")
                hand = update_hand(hand, word)
        if calculate_hand_len(hand) == 0:
            print("You got a 50 points bonus for using all letters!")
            current_sum += settings.BONUS_PTS
    if single:
        print("Game over! Total score: " + str(current_sum) + " points.")
    t.cancel()

    return current_sum


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    flag = 0
    with open('../data/game_settings.txt', 'r') as f:
        line = f.readline()
        nums = re.findall(r'\d+', line)
        settings.HAND_SIZE = int(nums[0])

    while True:
        let = input("Enter n to deal a new hand, r to replay the last hand, or e to end the game: ")
        if let == "n":
            hand = deal_hand(settings.HAND_SIZE)
            flag = 1
            play_hand(hand, word_list, settings.HAND_SIZE)
        elif let == "r" and flag == 0:
            print("You have not played a hand yet. Please play a new hand first!")
        elif let == "r" and flag == 1:
            play_hand(hand, word_list, settings.HAND_SIZE)
        elif let == "e":
            break
        else:
            print("Invalid command.")


if __name__ == '__main__':
    wordList = load_words_from_file()
    play_game(wordList)
