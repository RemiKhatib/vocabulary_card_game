import os

###########
# Constants
###########
nb_words=10   #Number of words which will be asked
list_columns=["Question", "Answer", "voice_q", "voice_a", "record_q", "record_a", "Class", "Ranking"]


#######################
# Directories and files
#######################
PROJECT_ROOT = os.path.dirname(__file__)

INPUT_DIR    = PROJECT_ROOT + "/inputs/"             # Inputs directory
OUTPUT_DIR   = PROJECT_ROOT + "/outputs/"            # Outputs directory
LIST_WORDS= "France_Viet-Nam_v2.csv"                    # Input file = List of words with their translation


