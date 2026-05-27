###########
# Libraries
###########
from config import *
from . import dictionnary
from . import card


def vocabulary_game():
    """Import the dictionnary"""
    filei = INPUT_DIR / LIST_WORDS
    print(f"Dictionnary used: {filei}\n")
    dict_full=dictionnary.load_file(filei)
    #print(dict_full)

    """"Selection of 10 words"""
    dict_sample=dictionnary.word_selection(dict_full)

    """Genrerate the GUI"""
    card.generate(dict_sample)


# Run the game
if __name__ == "__main__":
    vocabulary_game()

