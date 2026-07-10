"""
Synthetic voice generation module for the vocabulary game.

This module manages text-to-speech conversion using Google Text-to-Speech (gTTS)
to generate audio recordings of vocabulary words in multiple languages. Each word
recording is temporarily stored as an MP3 file and can be played back on demand.

Requires an active internet connection to generate voice recordings.
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
    Generate synthetic voice recordings for all selected vocabulary words.
    
    Creates audio files for both questions and answers from the provided word
    sample. Each word is converted to speech in its associated language.
    
    Args:
        selected_words (pd.DataFrame): DataFrame containing word pairs with columns:
                                      - Column 0: First language word
                                      - Column 1: Second language word
                                      - Column 2: Language code for column 0 word
                                      - Column 3: Language code for column 1 word
    
    Returns:
        tuple: Two lists of Voice objects:
               - records_q (list): Voice objects for question words
               - records_a (list): Voice objects for answer words
    
    Raises:
        Exception: If internet connection is unavailable or gTTS request fails.
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
    Generates and manages synthetic pronunciation of a single word.
    
    Uses Google Text-to-Speech (gTTS) to create an MP3 audio file of a word
    pronounced in the specified language. The audio file is stored temporarily
    and automatically deleted when the Voice object is destroyed.
    
    Requires an active internet connection to generate the voice recording.
    
    Attributes:
        record (str): File path to the generated MP3 audio file.
        tts (gtts.gTTS): The gTTS object managing the text-to-speech conversion.
    """

    def __init__(self, word, language):
        """
        Initialize and generate a voice recording for a word.
        
        Creates a synthetic pronunciation of the specified word in the given
        language using Google Text-to-Speech and saves it as an MP3 file.
        
        Args:
            word (str): The word to convert to speech.
            language (str): Language code (e.g., 'en', 'fr', 'vi') for the
                          text-to-speech conversion.
        
        Returns:
            None
        
        Raises:
            Exception: If internet connection is unavailable or gTTS fails
                      to generate the audio file.
        """

        self.record=OUTPUT_DIR + word + "_" + language + ".mp3"
        self.tts = gtts.gTTS(word, lang=language, slow=False)
        self.tts.save(self.record)

    def play(self):
        """
        Play the generated audio recording.
        
        Loads the MP3 audio file and plays it through the system's audio output.
        Blocks execution until playback completes.
        
        Returns:
            None
        
        Raises:
            FileNotFoundError: If the audio file has been deleted or does not exist.
            Exception: If audio playback fails due to missing audio device or
                      incompatible audio format.
        """

        play(pydub.AudioSegment.from_mp3(self.record))


    def __del__(self):
        """
        Clean up temporary audio file.
        
        Automatically called when the Voice object is destroyed. Deletes the
        temporary MP3 file from the outputs directory to free disk space.
        
        Returns:
            None
        """
        
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


