
"""
The aim to this module is to handle everything with the synthetic voice
"""

###########
# Libraries
###########
from config import *

import gtts
import os
import pydub
from   pydub.playback import play #play can only be used like that

import pandas as pd #Usefull only for the unitary tests


###########
# Functions
###########
def record_voices(selected_words):
    """
    Generates the audio files associated with every word of the selected dictionnary
    """
    records_q=[] #Questions
    records_a=[] #Answers
    for i in range(len(selected_words)) :
        records_q.append(Voice(selected_words.iloc[i,0], selected_words.iloc[i,2]))
        records_a.append(Voice(selected_words.iloc[i,1], selected_words.iloc[i,3]))

    return records_q, records_a

#########
# Classes
#########
class Voice :
    """
    Create a synthetic prounonciation of a word thanks to gTTS (needs an internet connexion).
    A temporary file is created in the outputs dir.
    """
    def __init__(self, word, language):
        self.record=OUTPUT_DIR + word + "_" + language + ".mp3"
        self.tts = gtts.gTTS(word, lang=language, slow=False)
        self.tts.save(self.record)

    def play(self):
        play(pydub.AudioSegment.from_mp3(self.record))


    def __del__(self):
        os.unlink(self.record)



if __name__ == "__main__" :
    #Creation of a minimal list to do the tests. Then test the synthetic voice.
    list_sample = [
        ["Chào","Bonjour"           , "vi", "fr", "", "", "", ""],
        ["Au revoir", "Tạm biệt"    , "fr", "vi", "", "", "", ""],
    ]
    df = pd.DataFrame(list_sample, columns=list_columns)
    print(df)

    #Records every words (Q =Questions, A=Answers)
    records_q, records_a = record_voices(df)

    #Test the voice for 2 words. One in French, the other one in Vietnamese
    for i in range(len(df)) :
        records_q[i].play()
        records_a[i].play()


