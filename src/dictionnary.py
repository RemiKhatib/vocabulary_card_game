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
    """Take n random words"""
    #The full dictionnary needs to be big enough
    if(len(dict_full)<n):
        print(f"Your dictionnary has less than {n} words. It cannot work.")
        quit()

    #Since we have pandas class, we cannot use random.sample directly
    indexes=rd.sample(range(len(dict_full)), n)
    return dict_full.iloc[indexes].reset_index(drop=True)



class cards:
    """
    Class associated with the words to find. They will be displayed on cards. On one side the question on the other side the answer.
    For each word :
     - The language the initial language of word is choosed randomly (0 or 1) in __init__.
     - When we return the card (retur_card), we see the other language.
     - At each step, the card is displayed (display)
    """
    def __init__(self, dict_sample):
        self.languageq=[]
        self.language=[]
        self.word=[]
        
        for i in range(len(dict_sample)):
            self.languageq.append(rd.choice(range(2)))                  #Language of the question
            self.language.append(self.languageq[i])                     #Actual language displayed on the card
            self.word.append(dict_sample.iloc[i,self.language[i]])         #Word displayed on the card
            #print(f"__init__: {self.languageq[i]} - {self.word[i]}")

    def return_card(self, dict_sample, index):
        self.language=(self.language+1)%2
        self.word=dict_sample.iloc[0,self.language]

    def display(self):
        return self.word


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
    
    #Test for language shuffling
    questions_list=cards(selected_words)
    print(f"Test for questions_list :\n{questions_list.display()}\n\n")

    pass