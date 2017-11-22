import sys
sys.path.append("..")
from ..Dianne import Note
import note_MIDI

a = note_MIDI.Note_MIDI(Note.Note.A_SHARP, 4)
print(a.noteOctaveTo_MIDI_Number())