from game_vs_comp import play_game
from erudite_game import load_words_from_file

if __name__ == '__main__':
    word_list = load_words_from_file()
    play_game()