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

n=10 # Number of questions

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
        self.root=root
        self.dict_sample=dict_sample
        self.root.title("🃏 Vocabulary game 🃏")
        self.root.geometry("900x500")
        self.root.configure(background="black")


        #Ratio of root boxes
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(1, weight=1)


        #Left Title "Question / Answer"
        self.l_title = tk.Label(self.root, text="Question / Answer", bg="red")
        self.l_title.grid(column=0, row=0, sticky="NSEW")
        #Left Word to find or found
        self.i = self.j = 0 #Indexes associated with the card to dispay (i) ans its face (j)
        self.l_qa = tk.Button(self.root, text=self.dict_sample.iloc[self.i,self.j], bg="yellow",
                            cursor="hand1", relief="raised", bd=2,
                            command=self.other_side)
        self.l_qa.grid(row=1, column=0, ipadx=10, ipady=10, sticky="NSEW")
        

        #Right Title "List of Questions / Answers"
        self.r_title = tk.Label(self.root, text="List of Questions / Answers", bg="blue")
        self.r_title.grid(column=1, row=0, ipadx=10, ipady=10, sticky="NSEW")
        #Right : "List of Questions / Answers"
        self.r_qa = tk.Frame(self.root, bg="green")
        self.r_qa.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")
        #I initialize a list of n labels in order to fix the place of the labels once for all.
        #When we draw a card, we will replace the empty text by the answer of the previous word.
        self.r_labels=[]
        self.r_words=[]
        print(self.r_words)
        for idx in range(n):
            self.r_words.append(tk.StringVar())
            self.r_label = tk.Label(self.r_qa, textvariable=f"{self.r_words[idx]}", bg="grey", anchor="w")
            self.r_label.pack(fill="x", expand=True, ipadx=5, ipady=5, padx=0, pady=0)
            self.r_labels.append(self.r_label)


        #Bottom : Button to pass the cards (new word)
        self.draw_btn = tk.Button(self.root, text="Next question", font=("Arial", 14, "bold"),bg="grey",
                                cursor="hand1", relief="raised", bd=2,
                                command=self.draw)
        self.draw_btn.grid(column=0, row=2, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")


    #Draw a new card / Ask a new question
    def draw(self):
        #Display the list of the QA on the right
        self.r_words[self.i].set(f"{self.dict_sample.iloc[self.i,0]} --> {self.dict_sample.iloc[self.i,1]}")


        #Display a new question on the left
        self.i+=1
        self.l_qa.config(text=self.dict_sample.iloc[self.i,0])




    #Check the answer
    def other_side(self):
        self.j=(self.j+1)%2
        self.l_qa.config(text=self.dict_sample.iloc[self.i,self.j])


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
    generate(df) #Display the first screen with the first question

