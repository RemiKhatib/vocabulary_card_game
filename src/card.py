"""
Contain everything about the GUI.
"""
#https://www.youtube.com/watch?v=xJZksz2UpqE

###########
# Libraries
###########
from config import *
from . import dictionnary

import tkinter as tk
import pandas as pd #Usefull only for the unitary tests

#######################
# Classes and functions
#######################

class AppFrame:
    """
    Class associated with the GUI
        
    The screen is divide in 5 regions :
        - Top left (small on x and y) : Title "Question / Answer"
        - Top right (big on x, small on y) : Title "List passed words"
        - Center left (small on x, big on y) : The word to find or the answer
        - Center left (big on x and y) : The list of the precedent QA
        - Bottom (full x and small y): Button to draw the next card (next question).
    """
    def __init__(self, root, dict_sample):
        #Main window caracteristics
        root.title("🃏 Vocabulary game 🃏")
        root.geometry("900x500")
        root.configure(background="black")


        #Ratio of root boxes
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.rowconfigure(1, weight=1)


        #Top left : Title "Question / Answer"
        tl_title = tk.Label(root, text="Question / Answer", bg="red")
        tl_title.grid(column=0, row=0, sticky="NSEW")
        #Center Left : Word to find or found
        cl_qa = tk.Label(root, text=dict_sample.iloc[0,0], bg="yellow")
        cl_qa.grid(row=1, column=0, ipadx=10, ipady=10, sticky="NSEW")
        

        #Top right : Title "List of Questions / Answers"
        tr_title = tk.Label(root, text="List of Questions / Answers", bg="blue")
        tr_title.grid(column=1, row=0, ipadx=10, ipady=10, sticky="NSEW")
        #Center right : "List of Questions / Answers"
        tr_qa = tk.Frame(root, bg="green")
        tr_qa.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")
        #l_words contains the list of words which will be asked. All the informations are stored.
        l_words=[]
        for i in range(10):
            l_word = tk.Label(tr_qa, text=f"l_word{i}", bg="grey", anchor="w")
            l_word.pack(fill="x", expand=True, ipadx=5, ipady=5, padx=0, pady=0)
            l_words.append(l_word)

        #Bottom : Button to pass the cards (new word)
        draw_btn = tk.Button(root, text="Next question", font=("Arial", 14, "bold"),bg="grey",
                                cursor="hand1", relief="raised", bd=2,
                                command=self.draw())
        draw_btn.grid(column=0, row=2, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")


    #Draw a new card / Ask a new question
    def draw(self):
        pass

    #Check the answer
    def other_side():
        pass



#------------------


def generate(dict_sample):
    """
    Main function of the card game.
      - Create the GUI
      - Handle the actions with the cards
    """
    root = tk.Tk()
    AppFrame(root, dict_sample)
    root.mainloop()


#------------------



#######
# Tests
#######
if __name__=="__main__":
    #Creation of a minimal list to do the tests. Then conversion into pandas.DataFrame.
    #The order between Vietnamese and French is mixed in order to reproduce the deck shuffling.
    list_sample = [
        ["Chào","Bonjour",  "Good morning / Good afternoon", ""],
        ["Au revoir", "Tạm biệt", "Good bye", ""],
        ["Cảm ơn", "Merci", "Thank you", ""],
        ["De rien", "Không có gì", "You are welcome", ""],
        ["Un", "Một", "One", ""],
        ["Deux", "Hai", "Two", ""],
        ["Ba", "Trois", "Three", ""],
        ["Bốn", "Quatre", "Four", ""],
        ["Cinq", "Năm", "Five", ""],
        ["Six", "Sáu", "Six", ""]
    ]
    df = pd.DataFrame(list_sample, columns=["Français", "Tiếng Việt", "English", "Emoji"])
    print(df)


    #Tests of the GUI with the fake pandas.DataFrame
    generate(df)
