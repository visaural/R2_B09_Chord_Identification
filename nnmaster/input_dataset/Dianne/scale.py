'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 1.3
author: Joachim Navarro, 2017

Zeroth-inversion-chord input dataset generator for use in neural networks.
'''

'''
scale.py
Contains the 12 note scale list.
'''

import Note
import ChordTypes

TWELVE_NOTE_SCALE = (Note.Note.C, Note.Note.C_SHARP, Note.Note.D, Note.Note.D_SHARP, Note.Note.E, Note.Note.F, Note.Note.F_SHARP, Note.Note.G, Note.Note.G_SHARP, Note.Note.A, Note.Note.A_SHARP, Note.Note.B)
NOTE_ABSOLUTE_POSITIONS = {Note.Note.C: 1, Note.Note.C_SHARP: 2, Note.Note.D: 3, Note.Note.D_SHARP: 4, Note.Note.E: 5, Note.Note.F: 6, Note.Note.F_SHARP: 7, Note.Note.G: 8, Note.Note.G_SHARP: 9, Note.Note.A: 10, Note.Note.A_SHARP: 11, Note.Note.B: 12}
CHORD_TYPES = (
ChordTypes.ChordTypes.MAJOR,
ChordTypes.ChordTypes.MINOR,
ChordTypes.ChordTypes.AUGMENTED,
ChordTypes.ChordTypes.DIMINISHED,
ChordTypes.ChordTypes.SUS2,
ChordTypes.ChordTypes.SUS4,
ChordTypes.ChordTypes.MAJOR_7,
ChordTypes.ChordTypes.MINOR_7,
ChordTypes.ChordTypes.DOMINANT_7,
ChordTypes.ChordTypes.AUG_7,
ChordTypes.ChordTypes.DIM_7,
ChordTypes.ChordTypes.HALF_DIM,
ChordTypes.ChordTypes.MAJOR_7_SUS2,
ChordTypes.ChordTypes.MAJOR_7_SUS4,
ChordTypes.ChordTypes.DOM_7_SUS2,
ChordTypes.ChordTypes.DOM_7_SUS4,
ChordTypes.ChordTypes.MAJOR_9,
ChordTypes.ChordTypes.MINOR_9,
ChordTypes.ChordTypes.DOMINANT_9,
ChordTypes.ChordTypes.AUG_9,
ChordTypes.ChordTypes.DIM_9,
ChordTypes.ChordTypes.MAJOR_9_SUS2,
ChordTypes.ChordTypes.MAJOR_9_SUS4,
ChordTypes.ChordTypes.DOM_9_SUS2,
ChordTypes.ChordTypes.DOM_9_SUS4,
ChordTypes.ChordTypes.MAJOR_11,
ChordTypes.ChordTypes.MINOR_11,
ChordTypes.ChordTypes.DOMINANT_11,
ChordTypes.ChordTypes.AUG_11,
ChordTypes.ChordTypes.MAJOR_11_SUS2,
ChordTypes.ChordTypes.DOM_11_SUS2,
ChordTypes.ChordTypes.MIN_MAJ_7,
ChordTypes.ChordTypes.MIN_MAJ_7_9,
ChordTypes.ChordTypes.MAJ_6,
ChordTypes.ChordTypes.MIN_6,
ChordTypes.ChordTypes.MAJ_6_9,
ChordTypes.ChordTypes.MIN_6_9
)