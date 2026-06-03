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
            dict_full = dict_full[dict_full["Français"] != ""].reset_index(drop=True)

    except FileNotFoundError:
        messagebox.showerror("Error", f"File {csv_file} not found.")
        self.root.quit()

    return dict_full.groupby("Français", dropna=False, sort=False).last().reset_index() # Duplicates managment

    
def word_selection(dict_full, n=10):
    """
    Take n random words in the dictionnary.
    Then shuffle the language in order to ask question in one language or another one.
    """
    #The full dictionnary needs to be big enough
    if(len(dict_full)<n):
        print(f"Your dictionnary has less than {n} words. It cannot work.")
        quit()

    #Since we have pandas class, we cannot use random.sample directly in order to select them
    #We have to pass by an idex selection
    indexes=rd.sample(range(len(dict_full)), n)
    selected_words=dict_full.iloc[indexes].reset_index(drop=True)

    #Shuffling
    for i in range(len(selected_words)):
        if rd.random()<0.5:
            selected_words.iloc[i,0], selected_words.iloc[i,1] = selected_words.iloc[i,1], selected_words.iloc[i,0]
        
    
    #Change column name of the selection
    #Column1=Question
    #Column2=Answers
    #The rest remains
    column=selected_words.columns.tolist()
    column[0]="Question"
    column[1]="Answer"
    selected_words.columns=column
    
    return selected_words



#######
# Tests
#######
if __name__=="__main__" :
    #Test for the length of the dictionnary
    #word_selection({0,1,2,3,4,5,6,7,8})    #Should be KO
    
    #Test for word_selection
    dictionnary=load_file(INPUT_DIR / LIST_WORDS)
    selected_words=word_selection(dictionnary)  #Should be OK if your dictionnary is big enough
    print(f"Test for selected_words :\n{selected_words}\n\n\n")  #Test if the order is random
   

    pass