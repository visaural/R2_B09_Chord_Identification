'''
NADINE
Neural Array Dataset Interpreter for Note Extrapolates
version 0.1
author: Joachim Navarro, 2017

Converts chord input file to data that can be interpreted by the ADNN.
'''

'''
chord_midi.py
Chord class, but with MIDI notes instead of chords.
'''

from ..Dianne import ChordTypes, Note

class Chord_MIDI:

    rootNote = None
    chordType = None
    MIDInotes = []

    def __init__(self, root, type, listOfMIDINotes):

        self.rootNote = root
        self.chordType = type
        for i in range(len(listOfMIDINotes)):
            self.MIDInotes.append(listOfMIDINotes[i])




