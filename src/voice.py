
"""
The aim to this module is to handle everything with the synthetic voice
"""

###########
# Libraries
###########
from config import *

import gtts
import pydub
from pydub.playback import play #play can only be used like that
import os


class Voice :
    """
    Create a synthetic prounonciation of a word thanks to gTTS (needs an internet connexion)
    Save it and then play it.
    The file can be removed
    """
    def __init__(self, word, language):
        self.record=OUTPUT_DIR + "word_" + language + ".mp3"
        self.tts = gtts.gTTS(word, lang=language, slow=False)
        self.tts.save(self.record)
        play(pydub.AudioSegment.from_mp3(self.record))

    def rm(self):
        os.unlink(self.record)



if __name__ == "__main__" :
    #Test the voice for 2 words. One in French, the other one in Vietnamese
    word1 = "Bonjour"
    lang1='fr'
    word2 = "Xin chào"
    lang2='vi'

    voice1=Voice(word1, lang1)
    voice2=Voice(word2, lang2)

    voice1.rm()
    voice2.rm()

