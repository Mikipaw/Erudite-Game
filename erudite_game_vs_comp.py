from erudite_game import *


def comp_choose_word(hand, word_list, n, difficulty ='i'):
    """
    Given a hand and a word_list, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the word_list.

    If no words in the word_list can be made from the hand, return None.

    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    shift = 1
    if difficulty == 'e':
        shift = 6
    elif difficulty == 'm':
        shift = 4
    elif difficulty == 'h':
        shift = 2

    best_score = 0
    best_word = None

    i = 0
    while i < len(word_list):
        if is_valid_word(word_list[i], hand, word_list):
            score = get_word_score(word_list[i], n)
            if score > best_score:
                best_score = score
                best_word = word_list[i]
        i += random.randint(1, shift)

    return best_word


def comp_play_hand(hand, word_list, n, single = True, difficulty = 'h'):
    """
    Returns total score that computer achieved.

    Allows the computer to play the given hand, following the same procedure
    as play_hand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. comp_choose_word returns None).

    hand: dictionary (string -> int)
    word_list: list (string)
    n: integer (HAND_SIZE; required for additional points)
    single: bool (default True)
    difficulty: str (default 'i')
    """

    total_score = 0
    while calculate_hand_len(hand) > 0:
        print("Current computer's hand: ", end=' ')
        display_hand(hand)
        word = comp_choose_word(hand, word_list, n, difficulty)
        if word is None:
            break

        else:
            if not is_valid_word(word, hand, word_list):
                print('This is signalizing that computer is dumb...')
                break
            else:
                score = get_word_score(word, n)
                total_score += score
                if single:
                    print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(total_score) + ' points')
                else:
                    print('Computer found ' + word + ' and get ' + str(score) + ' points...')
                hand = update_hand(hand, word)
                print()

    if single:
        print('Total score: ' + str(total_score) + ' points.')
    return total_score

def play_vs_comp(hand, word_list, n):
    """
    Allows the user to play the given hand again computer, as follows:

    Same rules as in single game, but user will compete against computer

    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    n: integer (HAND_SIZE; required for additional points)

    """

    number_of_rounds = int(input("Please, enter a number of rounds: "))

    while True:
        dif = input("Choose the difficulty: \n e - easy \n m - medium \n h - hard \n i - impossible \n")
        if dif in ['e', 'm', 'h', 'i']:
            user_pts = play_hand(hand, word_list, n, False, dif)
            comp_pts = comp_play_hand(hand, word_list, n, False, dif)
            number_of_rounds -= 1
            print("Round ended! \n Your points: " + str(user_pts) + "\n Computer's points: " + str(comp_pts))
            break
        else:
            print("Invalid input. Please, try again")

    while number_of_rounds > 0:
        hand = deal_hand(n)
        user_pts += play_hand(hand, word_list, n, False, dif)
        comp_pts += comp_play_hand(hand, word_list, n, False, dif)
        print("Round ended! \n Your points: " + str(user_pts) + "\n Computer's points: " + str(comp_pts))
        number_of_rounds -= 1

    if user_pts > comp_pts:
        print("Congratulations! You won the game!")
    elif user_pts < comp_pts:
        print("Unlucky today! You lost the game...")
    else:
        print("This is a draw today!")


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using comp_play_hand.

    4) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    flag = 0
    while True:
        letf = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if letf == "n":
            while True:
                lets = input("Enter u to have yourself play, c to have the computer play or n to play vs computer: ")
                if lets == "u":
                    hand = deal_hand(HAND_SIZE)
                    flag = 1
                    play_hand(hand, word_list, HAND_SIZE)
                    break
                elif lets == "c":
                    hand = deal_hand(HAND_SIZE)
                    flag = 1
                    comp_play_hand(hand, word_list, HAND_SIZE)
                    break
                elif lets == 'n':
                    hand = deal_hand(HAND_SIZE)
                    flag = 1
                    play_vs_comp(hand, word_list, HAND_SIZE)
                    break

                print("Invalid command")
        elif letf == "r" and flag == 1:
            while True:
                lets = input("Enter u to have yourself play, c to have the computer play or n to play vs computer: ")
                if lets == "u":
                    play_hand(hand, word_list, HAND_SIZE)
                    break
                elif lets == "c":
                    comp_play_hand(hand, word_list, HAND_SIZE)
                    break
                elif lets == 'n':
                    play_vs_comp(hand, word_list, HAND_SIZE)
                    break
                print("Invalid command")
        elif letf == "r" and flag == 0:
            print("You have not played a hand yet. Please play a new hand first!")
        elif letf == "e":
            break
        else:
            print("Invalid command")


if __name__ == '__main__':
    word_list = load_words_from_file()
    play_game(word_list)


