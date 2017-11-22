'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 1.3
author: Joachim Navarro, 2017

Zeroth-inversion-chord input dataset generator for use in neural networks.
'''

'''
chord.py
Chord class.
'''

import Note
import ChordTypes
import scale

class Chord():

    rootNote = None
    type = None
    scaleNotes = []
    pattern = []

    def __init__(self, r, t):
        '''
        Constructor for chord class.
        :param r: Note n.
        :param t: ChordTypes t from enum.
        '''

        self.rootNote = r
        self.type = t
        self.scaleNotes = []
        self.pattern = []
        self.absolutePositionNotes = []

        noteNum = r.value

        # Notes of the scale this chord is in
        for note in range(noteNum - 1, noteNum + 23):
            self.scaleNotes.append(Note.Note.noteToString(scale.TWELVE_NOTE_SCALE[note % 12]))

        for i in range(len(self.type.value)):
            self.pattern.append(self.scaleNotes[self.type.value[i] - 1])
            #print("Added " + self.scaleNotes[self.type.value[i] - 1] + " to pattern")
            #self.absolutePositionNotes.append(scale.NOTE_ABSOLUTE_POSITIONS[Note.Note.stringToNote(self.pattern[i])])

        # Append the indeces of the notes in the chord from self.scaleNotes

        self.scaleNotesSelection = 0
        self.patternSelection = 0

        while self.scaleNotesSelection < 24 and self.patternSelection < len(self.pattern):
            #print('Checking self.pattern', self.patternSelection)
            if self.scaleNotes[self.scaleNotesSelection] == self.pattern[self.patternSelection]:
                self.absolutePositionNotes.append(24 if (self.scaleNotesSelection + noteNum == 24) else (self.scaleNotesSelection + noteNum) % 24)
                self.patternSelection += 1

            self.scaleNotesSelection += 1


    def getPattern(self):
        '''
        Returns a list of notes in the chord.
        '''
        s = ""
        for n in self.pattern:
            s += (n + " ")
        return s

    def getAbsoluteNotePattern(self):
        '''
        Returns the numerical representations of the notes in the chord
        (C = 1, B = 12)
        '''
        s = ""
        for n in self.absolutePositionNotes:
            s += (str(n) + " ")
        return s


    def __repr__(self):
        return Note.Note.noteToString(self.rootNote) + ChordTypes.ChordTypes.chordTypeToString(self.type)
