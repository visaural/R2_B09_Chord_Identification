'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 1.3
author: Joachim Navarro, 2017

Zeroth-inversion-chord input dataset generator for use in neural networks.
'''

'''
dianne.py
Master file. Contains calls of functions and outputs the dataset file.
'''

import chord
import ChordTypes
import Note
import scale

chordsFile = None
chordObjectsList = []
chordsList = []
chordAbsolutePositionsList = []

subsetChordObjectsList = []
subsetChordsList = []

def generateChords():
    '''
    Constructs all possible chord objects as defined in ChordTypes.py and Note.py
    :return: Void
    '''
    for rootNote in scale.TWELVE_NOTE_SCALE:
        for chordType in scale.CHORD_TYPES:
            chordObjectsList.append(chord.Chord(rootNote, chordType))

    for a in range(len(chordObjectsList)):
        chordname = chordObjectsList[a].__repr__() + " "
        chordpat = chordObjectsList[a].getPattern()
        chordap = chordObjectsList[a].getAbsoluteNotePattern()
        chordsList.append(chordname + chordpat + "  " + chordap)
        #chordsList.append(chordname)

def writeToChordsFile():
    '''
    Writes list of chords to an output text file.
    :return: Void
    '''
    for i in chordsList:
        print(i)

    with open("../input_dataset.txt", 'w') as chordsFile:
        for i in chordsList:
            chordsFile.write(i)
            chordsFile.write("\n")

        chordsFile.write("\n\n\n" + "Number of chords: " + str(len(chordsList)))

    print("Written " + str(len(chordsList)) + " chords to file.")


# Main thread
if __name__ == "__main__":
    generateChords()
    writeToChordsFile()