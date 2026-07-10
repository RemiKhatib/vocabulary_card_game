"""
Configuration module for the vocabulary learning game.

This module defines global constants and file paths used throughout the application,
including game parameters, DataFrame column definitions, difficulty levels, and
directory/file locations.

Constants:
    nb_words (int): Number of vocabulary words to include in each game session.
    list_columns (list): Column names for the game DataFrame structure.
    LEVELS (list): Available difficulty levels based on word frequency rankings.

Directories:
    PROJECT_ROOT (str): Root directory of the project.
    INPUT_DIR (str): Directory containing input files (vocabularies, resources).
    OUTPUT_DIR (str): Directory for generated output files (audio recordings).

Files:
    LIST_WORDS (str): CSV file containing vocabulary words and translations.
"""

import os

###########
# Constants
###########
nb_words=10   #Number of words which will be asked
list_columns=["Question", "Answer", "voice_q", "voice_a", "record_q", "record_a", "Class", "Ranking"] #List of the columns of the final dataframe
LEVELS=[100,200,500,1000,"Full"] #Selection of the words according their occurence


#######################
# Directories and files
#######################
PROJECT_ROOT = os.path.dirname(__file__)

INPUT_DIR    = PROJECT_ROOT + "/inputs/"             # Inputs directory
OUTPUT_DIR   = PROJECT_ROOT + "/outputs/"            # Outputs directory
LIST_WORDS= "France_Viet-Nam_v2.csv"                    # Input file = List of words with their translation


