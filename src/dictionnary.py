"""
Classes and functions associated with the words :
- Loading dictionnary
- Choose the words which will be transleted
- Choose the language of the question and the one wich will be displayed

Contain everything to load the dictionnary
"""

###########
# Libraries
###########
from config import *

import pandas as pd
import random as rd


#######################
#######################
def load_file(csv_file):
    """ Load the csv file containing the different words."""
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            dict_full = pd.read_csv(f, dtype=str, sep=";").fillna("")
            #Empty row managment
            dict_full = dict_full[dict_full[dict_full.columns[0]] != ""].reset_index(drop=True) #If the first column is empty, we remove it.

    except FileNotFoundError:
        messagebox.showerror("Error", f"File {csv_file} not found.")
        self.root.quit()

    return dict_full.groupby(dict_full.columns[0], dropna=False, sort=False).last().reset_index() # Remove duplicates on the first column

    
def word_selection(dict_full):
    """
    Take nb_words random words in the dictionnary.
    Then shuffle the language in order to ask question in one language or another one.
    We also store the language in order to use synthetic voice
    """
    #The full dictionnary needs to be big enough
    if(len(dict_full)<nb_words):
        print(f"Your dictionnary has less than {n} words. It cannot work.")
        quit()

    #Since we have pandas class, we cannot use random.sample directly in order to select them
    #We have to pass by an index selection
    indexes=rd.sample(range(len(dict_full)), nb_words)
    selected_words=dict_full.iloc[indexes].reset_index(drop=True)

    #Shuffling + adding the language associated with every word
    voice_q , voice_a = [], []
    for i in range(len(selected_words)):
        if rd.random()<0.5:
            selected_words.iloc[i,0], selected_words.iloc[i,1] = selected_words.iloc[i,1], selected_words.iloc[i,0]
            voice_q.append(selected_words.columns[1])
            voice_a.append(selected_words.columns[0])
        else :
            voice_q.append(selected_words.columns[0])
            voice_a.append(selected_words.columns[1])

    selected_words.insert(2, list_columns[2], voice_q)
    selected_words.insert(3, list_columns[3], voice_a)
    #print(selected_words)
        
    
    #Change column name of the selection
    selected_words.columns=list_columns[0:4]+list_columns[6:8]
    
    return selected_words



def word_level(dict_full, level):
    """
    Select only the words which are desired according to the level.
    The level is the maximal ranking of a word. The higher the ranking, the most often it is used.
    """

    #Top level (not an integer)
    if(level==LEVELS[len(LEVELS)-1]):
        return dict_full

    #Level as an integer
    selected = dict_full[dict_full[list_columns[7]].astype(int) <= level]
    return selected



#######
# Tests
#######
if __name__=="__main__" :
    dictionnary=load_file(INPUT_DIR + LIST_WORDS)

    #=======================
    #Test the word_selection
    #=======================
    #Test for the length of the dictionnary
    #word_selection({0,1,2,3,4,5,6,7,8})    #Should be KO
    
    #Test for word_selection
    selected_words=word_selection(dictionnary)  #Should be OK if your dictionnary is big enough
    print(f"Test for word_selection :\n{selected_words}\n\n")  #Test if the order is random
    print("==================================================\n\n")


    #===============
    #Test word_level
    #===============
    #Minimal test
    selected_words=word_level(dictionnary, 5)
    print(f"Test for word_level (max=5):\n{selected_words}\n\n")  #Should display only the words with a maximal ranking of 5

    #Full test
    selected_words=word_level(dictionnary, LEVELS[len(LEVELS)-1])
    print(f"Full dictionnary")
    print(f"Number of words in the initial dictionnary {len(dictionnary)}")
    print(f"Number of words in the final dictionnary {len(selected_words)}\n\n") #The 2 dictionnaries should have the same size
        
    #Over the limits
    selected_words=word_level(dictionnary, 9999999999)
    print(f"Over the limits")
    print(f"Number of words in the initial dictionnary {len(dictionnary)}")
    print(f"Number of words in the final dictionnary {len(selected_words)}") #The 2 dictionnaries should have the same size


    pass