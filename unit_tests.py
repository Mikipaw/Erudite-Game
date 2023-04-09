from erudite_game import *


def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure = False
    words = {("", 7): 0, ("it", 7): 4, ("was", 7): 18, ("scored", 7): 54, ("waybill", 7): 155, ("outgnaw", 7): 127,
             ("fork", 7): 44, ("fork", 4): 94}

    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print("\tExpected", words[(word, n)],
                  "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
            failure = True

    if not failure:
        print("SUCCESS: test_get_word_score()")


def test_update_hand():
    """
    Unit test for update_hand
    """

    # test 1
    hand_orig = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    hand_copy = hand_orig.copy()
    word = "quail"

    hand2 = update_hand(hand_copy, word)
    expected_hand1 = {'l': 1, 'm': 1}
    expected_hand2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(hand_orig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return
    if hand_copy != hand_orig:
        print("FAILURE: test_update_hand('" + word + "', " + str(hand_orig) + ")")
        print("\tOriginal hand was", hand_orig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", hand_copy)

        return

    # test 2
    hand_orig = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    hand_copy = hand_orig.copy()
    word = "evil"

    hand2 = update_hand(hand_copy, word)
    expected_hand1 = {'v': 1, 'n': 1, 'l': 1}
    expected_hand2 = {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(hand_orig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return

    if hand_copy != hand_orig:
        print("FAILURE: test_update_hand('" + word + "', " + str(hand_orig) + ")")
        print("\tOriginal hand was", hand_orig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", hand_copy)

        return

    # test 3
    hand_orig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    hand_copy = hand_orig.copy()
    word = "hello"

    hand2 = update_hand(hand_copy, word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(hand_orig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return

    if hand_copy != hand_orig:
        print("FAILURE: test_update_hand('" + word + "', " + str(hand_orig) + ")")
        print("\tOriginal hand was", hand_orig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", hand_copy)

        return

    print("SUCCESS: test_update_hand()")


def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure = False

    # test 1
    word = "hello"
    hand_orig = get_frequency_dict(word)
    hand_copy = hand_orig.copy()

    if not is_valid_word(word, hand_copy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand_orig)

        failure = True

    if not is_valid_word(word, hand_copy, word_list):
        print("FAILURE: test_is_valid_word()")

        if hand_copy != hand_orig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", hand_orig, "but it is", hand_copy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_list?")
            word_in_list = word in word_list
            print("The word", word, "should be in word_list - is it?", word_in_list)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand_copy)

        failure = True

    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    word = "rapture"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

        # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
    word = "honey"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

        # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    word = "evil"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "even"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")

        failure = True

    if not failure:
        print("SUCCESS: test_is_valid_word()")


word_list = load_words_from_file()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("All done!")
