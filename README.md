> [!WARNING]  
> This program is under development.

**It is a game to learn vocabulary.**

**It takes as un input a dictionnary, select N words and ask you questions. You have the possibility to hear the prounonciation**

# Usage
Each time, one take a card with one word or sentence written on it.
You click on it and there is its translation with its pronounciation.
After N cards, the game is over and you have the list of the translated words/sentences.

You can put your own list of words to test yourself. Right now, the goal is to learn French or Vietnamese.


# How to install and use it ?
On linux, use makefile :
#### Virtual environment creation
```make venv```
#### Installation
```make install```
#### Run the programm
```make run```

or

```.venv/bin/python3 -m src.check_jobs ```
#### Clean the virtual environment and the compiled files
```make clean```
#### List all the targets of the makefile
```make help```


# List of modules
#### ./src/vocabulary.py
Main script which calls all the others. As mentionned, it allows you to learn vocabulary.
#### ./src/gui.py
Handle everything related with the GUI
#### ./src/dictionnary.py
Generate the list of words which will be asked
#### ./src/voice.py
Generate the synthetic voice.




# Future developments
  - [x] Create the main structure of the code
  - [x] Generate an input file
  - [x] Read a file with words and translation
  - [x] Mapping for the GUI
  - [x] Functions to define the main actions of the game
  - [x] Improving design
  - [x] Define the boundaries and make some securities in order to not go out.
  - [x] Use synth voice gtts
  - [ ] Generate the synthetic voices after the GUI loading in order to hide loading time
  - [ ] Make a longer dictionnary
  - [ ] List all the languages for gtts
  - [ ] Check what happens when texts is long
  - [ ] Check how to have emojis.
  - [ ] Have different levels and a different number of questions
  - [ ] Make the requirements

**This program has been created by Remi Khatib**
