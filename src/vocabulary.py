
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
from . import voice


def vocabulary_game():
    """
    Main function of the game. It calls all the other functions.
      - Selection of the questions
      - Generation of the synthetic voices
      - Generation of the GUI
    """
    #Import the dictionnary + select n words
    filei = INPUT_DIR + LIST_WORDS
    print(f"Dictionnary used: {filei}\n")
    dict_full=dictionnary.load_file(filei)
    #print(dict_full)

    #Selection of nb_words words
    dict_sample=dictionnary.word_selection(dict_full)

    #Synthtic voice generation
    records_q, records_a = voice.record_voices(dict_sample)
    dict_sample.insert(4, "record_q", records_q)
    dict_sample.insert(5, "record_a", records_a)
    #print(dict_sample)

    #Genrerate the GUI
    gui.generate(dict_sample)


# Run the game
if __name__ == "__main__":
    vocabulary_game()

