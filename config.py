import pathlib as pl

###########
# Constants
###########
nb_words=10   #Number of words which will be asked

#######################
# Directories and files
#######################
PROJECT_ROOT = pl.Path(__file__).parent
INPUT_DIR = PROJECT_ROOT / "inputs"              # Inputs directory
LIST_WORDS= "France_Viet-Nam.csv"                  # Input file = List of words with their translation


