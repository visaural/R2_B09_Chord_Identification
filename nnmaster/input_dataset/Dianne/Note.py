'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 2.0
author: Joachim Navarro, 2017

Zeroth-inversion-chord input dataset generator for use in neural networks.
'''

'''
Note.py
Note enumeration.
'''

from enum import Enum

class Note(Enum):
    C       = 1
    C_SHARP = 2
    D       = 3
    D_SHARP = 4
    E       = 5
    F       = 6
    F_SHARP = 7
    G       = 8
    G_SHARP = 9
    A       = 10
    A_SHARP = 11
    B       = 12

    def noteToString(n):
        if n == Note.C:
            return "C"
        elif n == Note.C_SHARP:
            return "C#"
        elif n == Note.D:
            return "D"
        elif n == Note.D_SHARP:
            return "D#"
        elif n == Note.E:
            return "E"
        elif n == Note.F:
            return "F"
        elif n == Note.F_SHARP:
            return "F#"
        elif n == Note.G:
            return "G"
        elif n == Note.G_SHARP:
            return "G#"
        elif n == Note.A:
            return "A"
        elif n == Note.A_SHARP:
            return "A#"
        elif n == Note.B:
            return "B"
        else:
            return "X"

    def stringToNote(n):
        if n == 'C':
            return Note.C
        elif n == 'C#':
            return Note.C_SHARP
        elif n == 'D':
            return Note.D
        elif n == 'D#':
            return Note.D_SHARP
        elif n == 'E':
            return Note.E
        elif n == 'F':
            return Note.F
        elif n == 'F#':
            return Note.F_SHARP
        elif n == 'G':
            return Note.G
        elif n == 'G#':
            return Note.G_SHARP
        elif n == 'A':
            return Note.A
        elif n == 'A#':
            return Note.A_SHARP
        elif n == 'B':
            return Note.B
        else:
            return None