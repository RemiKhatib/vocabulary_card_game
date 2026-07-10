"""
Vocabulary learning game module.

This program is a small game to learn vocabulary. It asks a series of questions
and allows users to check their answers by flipping cards.

The game workflow:
    1. Loads a dictionary from a file
    2. Allows the user to select a difficulty level
    3. Selects random words from the chosen level
    4. Generates synthetic voice recordings for questions and answers
    5. Displays an interactive GUI with flashcards
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
    Main function that orchestrates the vocabulary learning game.
    
    This function coordinates the entire game workflow:
        1. Loads the dictionary from the configured file
        2. Prompts user to select a difficulty level
        3. Filters words based on the selected level
        4. Randomly selects a sample of words
        5. Generates synthetic voice recordings for questions and answers
        6. Creates and displays the interactive GUI with flashcards
    
    Returns:
        None
    
    Raises:
        FileNotFoundError: If the dictionary file is not found at the configured path.
        Exception: If voice generation or GUI creation fails.
    """
    
    #Import the dictionnary + select n words
    filei = INPUT_DIR + LIST_WORDS
    print(f"Dictionnary used: {filei}\n")
    dict_full=dictionnary.load_file(filei)
    #print(dict_full)


    #Selection of the level of difficulty.
    level=gui.levelselection()
    dict_level=dictionnary.word_level(dict_full, level)


    #Selection of nb_words words
    dict_sample=dictionnary.word_selection(dict_level)

    #Synthtic voice generation
    records_q, records_a = voice.record_voices(dict_sample)
    dict_sample.insert(4, "record_q", records_q)
    dict_sample.insert(5, "record_a", records_a)
    #print(dict_sample)

    #=============================================================================
    #After this point, the Pandas.DataFrame has the colums defined in list_columns
    #=============================================================================

    #Genrerate the GUI
    gui.generate(dict_sample)


# Run the game
if __name__ == "__main__":
    vocabulary_game()

