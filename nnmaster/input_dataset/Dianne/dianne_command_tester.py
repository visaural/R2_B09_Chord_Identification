'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 1.3
author: Joachim Navarro, 2017

Given an input chord name, outputs the notes of that chord in the zeroth inversion.
'''

'''
dianne_command_tester.py
Tester for all classes, functions, and logic in DIANNE.
'''

import dianne
import chord
import ChordTypes
import Note
import scale

chordObjectsList = []

if __name__ == "__main__":

    x = chord.Chord(Note.Note.F_SHARP, ChordTypes.ChordTypes.AUGMENTED)
    print(x.pattern)

    for rootNote in scale.TWELVE_NOTE_SCALE:
        for chordType in scale.CHORD_TYPES:
            chordObjectsList.append(chord.Chord(rootNote, chordType))

    print(chordObjectsList[0].pattern)
