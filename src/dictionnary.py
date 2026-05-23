#Contain everything to load the dictionnary

###########
# Libraries
###########
from dataclasses import dataclass, asdict
from typing import Optional, Dict, List
import pandas as pd


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

    
