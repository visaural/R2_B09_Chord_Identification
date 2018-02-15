'''
NADINE
Neural Array Dataset Interpreter for Note Extrapolates
version 0.1
author: Joachim Navarro, 2017

Converts chord input file to data that can be interpreted by the ADNN.
'''

'''
loc_note_MIDI.py
MIDI note class.
'''

#from ..Dianne import Note

class Loc_Note_MIDI:

    note_obj = None
    note_octave = None

    def __init__(self, n, o):
        self.note_obj = n
        self.octave = o

    def noteOctaveTo_MIDI_Number(self):
        midinum = (12 * self.note_octave) + (self.note_obj.value - 1)
        return midinum

    @staticmethod
    def midiNumToNote(n):
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return notes[(n % 12)]
