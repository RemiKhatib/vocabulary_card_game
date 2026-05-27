#Contain everything to load the dictionnary

###########
# Libraries
###########
from config import *

from dataclasses import dataclass, asdict
from typing import Optional, Dict, List
import pandas as pd
import random as rd



@dataclass
class word:
    l1: str
    l2: str
    l3: str
    picture: Optional[str] = None


def load_file(csv_file):
    """ Load the csv file containing the different files."""
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


if __name__=="__main__" :
    #Test for the length of the dictionnary
    #word_selection({0,1,2,3,4,5,6,7,8}) #Should be KO
    word_selection(load_file(INPUT_DIR / LIST_WORDS)) #Should be OK if your dictionnary is big enough

    #Test for word_selection.
    print(word_selection(load_file(INPUT_DIR / LIST_WORDS))) #Test if the order is random
    
    pass