"""
Contain everything about the GUI.
"""


###########
# Libraries
###########
from config import *
from . import dictionnary
from . import voice

import tkinter as tk
import tkinter.messagebox

import pandas as pd #Usefull only for the unitary tests


#######################
# Classes and functions
#######################

class AppFrame:
    """
    Class associated with the GUI
        
    The screen is divide in 5 regions :
        - Top left (small on x and y) : Title "Question / Answer" + Synthetic voice
        - Top right (big on x, small on y) : Title "List passed words"
        - Center left (small on x, big on y) : The word to find or the answer
        - Center left (big on x and y) : The list of the precedent QA
        - Bottom (full x and small y): Button to draw the next card (next question).
    """

    word_class=list_columns[6] #"Class"

    #Fonts
    title_fonts=("Arial", 16, "bold", "underline")
    norm_fonts=("Arial", 14)

    #Colors
    l_qa_bg1="wheat"
    l_qa_abg1="wheat3"
    l_qa_bg2="rosybrown1"
    l_qa_abg2="rosybrown3"


    def __init__(self, root, dict_sample):
        #Main window caracteristics
        self.root=root
        self.dict_sample=dict_sample
        self.root.title("🇫🇷 Vocabulary game 🇻🇳")
        self.root.geometry("900x500")
        self.root.configure(background="black")

        #Ratio of root boxes
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(1, weight=1)

        #Word initialization
        self.i = self.j = 0 #Indexes associated with the card to dispay (i) ans its face (j)


        ##########
        #Left side
        ##########
        #Left Title "Question / Answer" with the possibility to play sound
        icon = tk.PhotoImage(file = "inputs/icons/sound.png")
        self.sound = icon.subsample(20,20)
        self.l_title = tk.Button(   self.root, text="Question / Answer", font=self.title_fonts,
                                    image=self.sound, compound='right',
                                    bg="burlywood2", relief="groove", bd=2,
                                    command=self.play
                                )
        self.l_title.grid(column=0, row=0, sticky="NSEW")


        #Left Word to find or found
        self.l_qa = tk.Button(  self.root,
                                text=self.display_question(),
                                font=self.norm_fonts,
                                bg=self.l_qa_bg1,
                                activebackground=self.l_qa_abg1,
                                cursor="hand1", relief="raised", bd=4,
                                command=self.other_side
                            )
        self.l_qa.grid(row=1, column=0, ipadx=10, ipady=10, sticky="NSEW")
        

        ###########
        #Right side
        ###########
        #Right Title "List of Questions / Answers"
        self.r_title = tk.Label(    self.root,
                                    text="List of previous words",
                                    font=self.title_fonts,
                                    bg="royalblue1",
                                    relief="groove",
                                    bd=2
                                )
        self.r_title.grid(column=1, row=0, ipadx=10, ipady=10, sticky="NSEW")

        #Right : "List of Questions / Answers"
        self.r_qa = tk.Frame(self.root, bg="lightblue2")
        self.r_qa.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")

        #I initialize a list of n labels in order to fix the place of the labels once for all.
        #When we draw a card, we will replace the empty text by the answer of the previous word.
        self.r_labels=[]
        self.r_words=[]
        for idx in range(nb_words):
            self.r_words.append(tk.StringVar())
            self.r_label = tk.Label(    self.r_qa,
                                        textvariable=f"{self.r_words[idx]}",
                                        font=self.norm_fonts,
                                        bg="lightblue2",
                                        anchor="w"
                                    )
            self.r_label.pack(fill="x", expand=True, ipadx=5, ipady=5, padx=0, pady=0)
            self.r_labels.append(self.r_label)

        #######
        #Bottom
        #######
        #Button to pass the cards (new word)
        self.draw_btn = tk.Button(self.root, text="Next question", font=("Arial", 16, "bold"),bg="grey",
                                cursor="hand1", relief="raised", bd=2,
                                command=self.draw)
        self.draw_btn.grid(column=0, row=2, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")


    #Draw a new card / Ask a new question
    def draw(self):
        #Display the list of the QA on the right
        self.r_words[self.i].set(f"{self.i+1} : {self.dict_sample.iloc[self.i,0]} → {self.dict_sample.iloc[self.i,1]}")

        #Display a new question on the left
        if self.i < nb_words-1 :
            self.i+=1
            self.j=0
            self.l_qa.config(   text=self.display_question(),
                                bg=self.l_qa_bg1,
                                activebackground=self.l_qa_abg1
                            )
        
        else :
            tkinter.messagebox.showinfo(message="It is the end of the game. Please close it.")



    #Check the answer
    def other_side(self):
        self.j=(self.j+1)%2
        if self.j==0 :
            bg=self.l_qa_bg1
            abg=self.l_qa_abg1
        else :
            bg=self.l_qa_bg2 
            abg=self.l_qa_abg2
        self.l_qa.config(   text=self.display_question(),
                            bg=bg,
                            activebackground=abg
                        )

    #Play the sound
    def play(self):
        try:
            self.dict_sample.iloc[self.i, self.j+4].play()
        except :
            print("No sound available.")

    #Display the question card of the word
    def display_question(self):
        if(self.dict_sample.loc[self.i,self.word_class] == ""):
            return f"{self.dict_sample.iloc[self.i,self.j]}\n\n\n"
        else:
            return f"{self.dict_sample.iloc[self.i,self.j]}\n\n\n({self.dict_sample.loc[self.i,self.word_class]})"


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
        ["Chào","Bonjour"           , "vi", "fr", "", "", "Nom", ""],
        ["Au revoir", "Tạm biệt"    , "fr", "vi", "", "", "", ""],
        ["Cảm ơn", "Merci"          , "vi", "fr", "", "", "Nom", ""],
        ["De rien", "Không có gì"   , "fr", "vi", "", "", "", ""],
        ["Un", "Một"                , "fr", "vi", "", "", "Nombre", ""],
        ["Deux", "Hai"              , "fr", "vi", "", "", "Nombre", ""],
        ["Ba", "Trois"              , "vi", "fr", "", "", "Nombre", ""],
        ["Bốn", "Quatre"            , "vi", "fr", "", "", "Nombre", ""],
        ["Cinq", "Năm"              , "fr", "vi", "", "", "Nombre", ""],
        ["Six", "Sáu"               , "fr", "vi", "", "", "Nombre", ""]
    ]
    df = pd.DataFrame(list_sample, columns=list_columns)
    print(df)

    #Tests of the GUI with the fake pandas.DataFrame
    generate(df) #Display the first screen with the first question

