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

    """Genrerate the card game"""
    card.generate(dict_full)


# Run the game
if __name__ == "__main__":
    vocabulary_game()

