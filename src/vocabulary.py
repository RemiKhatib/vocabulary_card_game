
"""
This program is a small game to learn vocabulary.
It asks few questions and you can check your answers by swapping a card.
"""
###########
# Libraries
###########
from config import *
from . import dictionnary
from . import gui


def vocabulary_game():
    """Import the dictionnary"""
    filei = INPUT_DIR / LIST_WORDS
    print(f"Dictionnary used: {filei}\n")
    dict_full=dictionnary.load_file(filei)
    #print(dict_full)

    """"Selection of 10 words"""
    dict_sample=dictionnary.word_selection(dict_full)

    """Genrerate the GUI"""
    gui.generate(dict_sample)


# Run the game
if __name__ == "__main__":
    vocabulary_game()

