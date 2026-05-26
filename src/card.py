#Contain everything about the game of cards.
#https://www.youtube.com/watch?v=xJZksz2UpqE

###########
# Libraries
###########
import tkinter as tk
import random

class AppCard:
    """Class associated with the GUI"""
    def __init__(self,root):
        #Main window caracteristics
        root.title("🃏 Vocabulary card game 🃏")
        root.geometry("900x500")
        root.configure(background="black")

        """
        The screen is divide in 5 regions :
          - Top left (small on x and y) : Title "Question / Answer"
          - Top right (big on x, small on y) : Title "List passed words"
          - Center left (small on x, big on y) : The word to find or the answer
          - Center left (big on x and y) : The list of the precedent QA
          - Bottom (full x and small y): Button to draw the next card (next question).
        """

        #Ratio of root boxes
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.rowconfigure(1, weight=1)

        #Top left : Title "Question / Answer"
        tl_title = tk.Label(root, text="Question / Answer", bg="red")
        tl_title.grid(column=0, row=0, sticky="NSEW")
        #Center Left : Word to find or found
        cl_qa = tk.Label(root, text="Example of word", bg="yellow")
        cl_qa.grid(row=1, column=0, ipadx=10, ipady=10, sticky="NSEW")
        

        #Top right : Title "List of Questions / Answers"
        tr_title = tk.Label(root, text="List of Questions / Answers", bg="blue")
        tr_title.grid(column=1, row=0, ipadx=10, ipady=10, sticky="NSEW")
        #Center right : "List of Questions / Answers"
        tr_qa = tk.Label(root, text="Temporary example", bg="green")
        tr_qa.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")


        #Bottom : Button to pass the cards (new word)
        draw_btn = tk.Button(root, text="Next question", font=("Arial", 14, "bold"),bg="grey",
                                cursor="hand1", relief="raised", bd=2,
                                command=self.draw())
        draw_btn.grid(column=0, row=2, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")


    def draw(self):
        pass

    def other_side():
        pass



##################


def generate(dict_full):
    """
    Main function of the card game.
      - Generate the card game
      - Allow to draw return the cards
      - Display some selected words
    """
    root = tk.Tk()
    AppCard(root)
    root.mainloop()


##################


if __name__=="__main__":
    generate(None)
