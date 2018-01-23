'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 1.3
author: Joachim Navarro, 2017

Zeroth-inversion-chord input dataset generator for use in neural networks.
'''

'''
ChordTypes.py
Contains enumeration of chord types with relative chromatic mappings. (Root = 1)
Also contains a representation method.
'''

from enum import Enum

NUMBER_OF_CHORD_TYPES = 37
NUMBER_OF_CHORDS = 12 * NUMBER_OF_CHORD_TYPES

'''
NOTE    C    C#    D    D#    E    F    F#    G    G#    A    A#    B    
#NUM    1    2     3    4     5    6    7     8    9     10   11    12
        13   14    15   16    17   18   19    20   21    22   23    24
'''

class ChordTypes(Enum):
    # Triads
    MAJOR           = (1, 5, 8)
    MINOR           = (1, 4, 8)
    AUGMENTED       = (1, 5, 9)
    DIMINISHED      = (1, 4, 7)
    SUS2            = (1, 3, 8)
    SUS4            = (1, 6, 8)

    # 7-based
    MAJOR_7         = (1, 5, 8, 12)
    MINOR_7         = (1, 4, 8, 11)
    DOMINANT_7      = (1, 5, 8, 11)
    AUG_7           = (1, 5, 9, 11)
    DIM_7           = (1, 4, 7, 10)
    HALF_DIM        = (1, 4, 7, 11)
    MAJOR_7_SUS2    = (1, 3, 8, 12)
    MAJOR_7_SUS4    = (1, 6, 8, 12)
    DOM_7_SUS2      = (1, 3, 8, 11)
    DOM_7_SUS4      = (1, 6, 8, 11)

    # 9-based
    MAJOR_9         = (1, 5, 8, 12, 15)
    MINOR_9         = (1, 4, 8, 11, 15)
    DOMINANT_9      = (1, 5, 8, 11, 15)
    AUG_9           = (1, 5, 9, 11, 15)
    DIM_9           = (1, 4, 7, 10, 15)
    MAJOR_9_SUS2    = (1, 3, 8, 12, 15)
    MAJOR_9_SUS4    = (1, 6, 8, 12, 15)
    DOM_9_SUS2      = (1, 3, 8, 11, 15)
    DOM_9_SUS4      = (1, 6, 8, 11, 15)

    # 11-based
    MAJOR_11        = (1, 5, 8, 12, 15, 18)
    MINOR_11        = (1, 4, 8, 11, 15, 18)
    DOMINANT_11     = (1, 5, 8, 11, 15, 18)
    AUG_11          = (1, 5, 9, 11, 15, 18)
    MAJOR_11_SUS2   = (1, 3, 8, 12, 15, 18)
    DOM_11_SUS2     = (1, 3, 8, 11, 15, 18)

    # Special
    MIN_MAJ_7       = (1, 4 ,8, 12)
    MIN_MAJ_7_9     = (1, 4, 8, 12, 15)
    MAJ_6           = (1, 5, 8, 10)
    MIN_6           = (1, 4, 8, 10)
    MAJ_6_9         = (1, 5, 8, 10, 15)
    MIN_6_9         = (1, 4, 8, 10, 15)


    def chordTypeToString(ct):

        if ct == ChordTypes.MAJOR:
            return "maj"
        elif ct == ChordTypes.MINOR:
            return "min"
        elif ct == ChordTypes.AUGMENTED:
            return "aug"
        elif ct == ChordTypes.DIMINISHED:
            return "dim"
        elif ct == ChordTypes.SUS2:
            return "sus2"
        elif ct == ChordTypes.SUS4:
            return "sus4"
        elif ct == ChordTypes.MAJOR_7:
            return "M7"
        elif ct == ChordTypes.MINOR_7:
            return "m7"
        elif ct == ChordTypes.DOMINANT_7:
            return "7"
        elif ct == ChordTypes.AUG_7:
            return "aug7"
        elif ct == ChordTypes.DIM_7:
            return "dim7"
        elif ct == ChordTypes.HALF_DIM:
            return "o7"
        elif ct == ChordTypes.MAJOR_7_SUS2:
            return "M7sus2"
        elif ct == ChordTypes.MAJOR_7_SUS4:
            return "M7sus4"
        elif ct == ChordTypes.DOM_7_SUS2:
            return "7sus2"
        elif ct == ChordTypes.DOM_7_SUS4:
            return "7sus4"
        elif ct == ChordTypes.MAJOR_9:
            return "M9"
        elif ct == ChordTypes.MINOR_9:
            return "m9"
        elif ct == ChordTypes.DOMINANT_9:
            return "9"
        elif ct == ChordTypes.AUG_9:
            return "aug9"
        elif ct == ChordTypes.DIM_9:
            return "dim9"
        elif ct == ChordTypes.MAJOR_9_SUS2:
            return "M9sus2"
        elif ct == ChordTypes.MAJOR_9_SUS4:
            return "M9sus4"
        elif ct == ChordTypes.DOM_9_SUS2:
            return "9sus2"
        elif ct == ChordTypes.DOM_9_SUS4:
            return "9sus4"
        elif ct == ChordTypes.MAJOR_11:
            return "M11"
        elif ct == ChordTypes.MINOR_11:
            return "m11"
        elif ct == ChordTypes.DOMINANT_11:
            return "11"
        elif ct == ChordTypes.AUG_11:
            return "aug11"
        elif ct == ChordTypes.MAJOR_11_SUS2:
            return "M11sus2"
        elif ct == ChordTypes.DOM_11_SUS2:
            return "11sus2"
        elif ct == ChordTypes.MIN_MAJ_7:
            return "mM7"
        elif ct == ChordTypes.MIN_MAJ_7_9:
            return "mM7(9)"
        elif ct == ChordTypes.MAJ_6:
            return "M6"
        elif ct == ChordTypes.MIN_6:
            return "m6"
        elif ct == ChordTypes.MAJ_6_9:
            return "M6(9)"
        elif ct == ChordTypes.MIN_6_9:
            return "m6(9)"
        else:
            return "XC"
