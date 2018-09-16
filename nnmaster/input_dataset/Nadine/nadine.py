'''
NADINE
Neural Array Dataset Interpreter for Note Extrapolates
version 1.0
author: R2-B09, 2017

Converts chord input file to data that can be interpreted by the ANN.

Citations:
kushalbhabra (2013). pyMidi [GitHub repository]. Retrieved November 17, 2017, from
    https://github.com/kushalbhabra/pyMidi.

Tang, S. (n.d.) Python code raw data from a MIDI controller. Retrieved from
    http://www.stephentang.io/python-code-raw-data-from-a-midi-controller/
'''

'''
nadine.py
Main file.
'''

import sys
import loc_note_MIDI
#import pygame
#from pygame import midi
#from pygame.locals import *

sys.path.insert(0, "../Dianne/")

INPUT_FILE = "../input_dataset.txt"
NUM_CHORDS = 444
outputFile = None
chordsList = []
chordTypesList = []
chordObjectsList = []
chordPossList = []
chordBoolsList = []
chordMIDINumbersList = []

def chordmap_2(input_file, WRITE_TO_OUTPUT_FILE):
    # STEP 1: MAKE LIST OF CHORDS
    input_notes = open(INPUT_FILE)
    # chordsList, chordTypesList = [i.strip().split(' ') for i in input_notes]

    chordsList = ([i.strip().split() for i in input_notes])

    for i in range(4):
        chordsList.pop()

    print(chordsList)
    print(len(chordsList))

    # STEP 2: MAKE LIST OF POSITIONS
    for chord in chordsList:
        # Numbers at which chord notes are (1 = C, 2 = C#...)
        chord_notes = []

        for s in chord:
            try:
                # Try converting the string to a number
                num = int(s)
                # Append the positions
                chord_notes.append(num)
            except:
                # Go to next element if the string can't be converted to a number
                pass
        chordPossList.append(chord_notes)

    print(chordPossList)
    print(len(chordPossList))

    # STEP 3: CONVERT NOTE NUMBER DISTANCES TO MIDI NUMBERS
    for chord_iteration in range(len(chordPossList)): # All chord types
        chordMIDINumbersList.append([])
        for oct_num in range(11):                     # All possible MIDI octaves
            temp = []
            for note_num in range(len(chordPossList[chord_iteration])):     # for each number in [1, 5, 8] for example
                 # if note_num is not 0:
                 #     if chordPossList[chord_iteration][note_num - 1] > chordPossList[chord_iteration][note_num]:   # Chord note MIDI num entries must be in ascending order
                 #         print("In " + str(chordPossList[chord_iteration]) + ", " + str(chordPossList[chord_iteration][note_num - 1]) + " is greater than " + str(chordPossList[chord_iteration][note_num]) + ", adding 23")
                 #         temp.append((12 * oct_num) + (chordPossList[chord_iteration][note_num] + 23))
                 #     else:
                 #         temp.append((12 * oct_num) + (chordPossList[chord_iteration][note_num] - 1))
                 # else:
                    temp.append((12 * oct_num) + (chordPossList[chord_iteration][note_num] - 1))

            chordMIDINumbersList[chord_iteration].append(temp)

    print(chordMIDINumbersList)
    print(len(chordMIDINumbersList))
    print(str(count3DLayeredList2D(chordMIDINumbersList)))

    # STEP 4: DELETE UNNEEDED (n > 127) CHORDS FROM DATABASE


def count3DLayeredList2D(ll):
    k = 0
    for a in range(len(ll)):
        for b in range(len(ll[a])):
            k += 1
    return k

def chordmap(input_file, WRITE_TO_OUTPUT_FILE):

    # STEP 1: MAKE LIST OF CHORDS
    input_notes = open(INPUT_FILE)
    #chordsList, chordTypesList = [i.strip().split(' ') for i in input_notes]

    chordsList = ([i.strip().split() for i in input_notes])

    for i in range(4):
        chordsList.pop()

    print(chordsList)
    print(len(chordsList))

    # STEP 2: MAKE LIST OF POSITIONS
    for chord in chordsList:
        # Numbers at which chord notes are (1 = C, 2 = C#...)
        chord_notes = []

        for s in chord:
            try:
                # Try converting the string to a number
                num = int(s)
                # Append the positions
                chord_notes.append(num)
            except:
                # Go to next element if the string can't be converted to a number
                pass
        chordPossList.append(chord_notes)

    print(chordPossList)
    print(len(chordPossList))

    # STEP 3: MAKE LIST OF BINARY POSITIONS
    for _set_ in range(len(chordPossList)):
        poss = []
        # Put a 1 or 0 in the position
        for i in range(24):
            if (i + 1) in chordPossList[_set_]:
                poss.append(1)
            else:
                poss.append(0)

        chordBoolsList.append(poss)

    print(chordBoolsList)
    print(len(chordBoolsList))

    if WRITE_TO_OUTPUT_FILE:
        writeToChordsFile(chordsList, chordBoolsList)


def writeToChordsFile(CL, CBL):

    SPACE_LENGTH = 10
    try:
        with open("../input_dataset_binaries.txt", 'w') as chordsFile:
            for i in range(len(CL)):
                chordsFile.write(CL[i][0] + ((SPACE_LENGTH - len(CL[i][0])) * " "))
                for j in range(24):
                    chordsFile.write(str(CBL[i][j]) + " ")
                chordsFile.write("\n")

    except Exception as e:
        print(e)

    printEqualElements(CBL, CL)

def anyTwoElementsEqual(CBL, CL):
    for i in range(len(CBL)):
        for j in range(i + 1, len(CBL)):
            if CBL[i] == CBL[j]:
                print(CL[i][0], "and", CL[j][0])
                return True

    return False

def printEqualElements(CBL, CL):

    if not anyTwoElementsEqual(CBL, CL):
        print("No two chords have equal mappings.")
    else:
        ee = []
        for i in range(len(CBL)):
            for j in range(i + 1, len(CBL)):
                if CBL[i] == CBL[j]:
                    print(CL[i][0], "and", CL[j][0])
                    ee.append(CL[i][0])
                    ee.append(CL[j][0])

        print(len(ee) // 2)

def realTimeMIDIChords():
    '''
    Displays the mappings of the notes currently being played on MIDI.
    (kushalbhabra, 2013; Tang, n.d.)
    '''
    # display a list of MIDI devices connected to the computer
    # this function written by Stephen Tang (n.d.), stephentang.io
    def print_device_info():
        for i in range(pygame.midi.get_count()):
            r = pygame.midi.get_device_info(i)
            (interf, name, input, output, opened) = r
            in_out = ""
            if input:
                in_out = "(input)"
            if output:
                in_out = "(output)"
            print("%2i: interface: %s, name: %s, opened: %s %s" %
                  (i, interf, name, opened, in_out))

    pygame.init()

    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    pygame.midi.init()

    print("Available MIDI devices:")
    print_device_info()

    MI = int(input("Select device ID: "))  # 2 the default for Project-X99

    '''
    Examples for Project-X99:
    INPUT 2: Komplete Kontrol 1
    INPUT 3: Komplete Kontrol EXT
    INPUT 4: Komplete Kontrol DAW
    '''

    input_id = MI
    midi_in = pygame.midi.Input(input_id)

    pygame.display.set_caption("midi test")
    screen = pygame.display.set_mode((400, 300), RESIZABLE, 32)

    print("Initializing realtime poll process.")
    realtime = True

    currentNoteNumbersInChord = []  # Current MIDI note #s in chord
    currentNotesInChord = []        # Binary mapping of notes in chord
    currentNoteNamesInChord = []    # Current note names in chord
    for i in range(24):
        currentNotesInChord.append(0)
    print("initialize:\n", currentNotesInChord, "length:" + str(len(currentNotesInChord)))

    while realtime:
        # pygame event handling
        events = event_get()
        for e in events:
            if e.type in [QUIT]:
                realtime = False
            if e.type in [KEYDOWN]:
                realtime = False

        if midi_in.poll():
            midi_events = midi_in.read(10)

            # MIDI NOTE ON
            if 0x90 <= midi_events[0][0][0] <= 0x9F:
                mod = 1
                if len(currentNotesInChord) != 24:
                    print("Error - length of array is not 24! Emergency stop.")
                    realtime = False
                    break

                # Add note number to current note numbers in chord
                currentNoteNumbersInChord.append(midi_events[0][0][1])

                # Add note to binary list
                root = currentNoteNumbersInChord[0] % 12
                # print("root:", str(root))
                # print("last element of currentNoteNumbersInChord:", currentNoteNumbersInChord[-1])
                # print("current note added:", midi_events[0][0][1])
                try:
                    currentNotesInChord[(root) + (currentNoteNumbersInChord[-1] - currentNoteNumbersInChord[0])] = 1
                except IndexError:
                    currentNotesInChord[midi_events[0][0][1] % 12] = 1

                # Add note being played
                currentNoteNamesInChord.append(loc_note_MIDI.Loc_Note_MIDI.midiNumToNote(midi_events[0][0][1]))

                print(currentNotesInChord)
                print(currentNoteNumbersInChord)
                print(currentNoteNamesInChord)

            # MIDI NOTE OFF
            elif 0x80 <= midi_events[0][0][0] <= 0x8F:
                print("Purging variables.")
                currentNotesInChord = []
                for i in range(24): currentNotesInChord.append(0)
                currentNoteNumbersInChord = []
                currentNoteNamesInChord = []

            # Aftertouch
            elif 0xD0 <= midi_events[0][0][0] <= 0xDF:
                pass

            # Something else except aftertouch
            else:
                print("Something else was tinkered.")
                print(midi_events[0][0][0])

    print("Exiting.")
    midi_in.close()
    pygame.midi.quit()
    pygame.quit()
    exit()

if __name__ == "__main__":

    print("Real-time MIDI to ANN Input Interpreter")

    choice = input("Generate chord file? [v1/v2/n]: ")
    if choice in ['v1', 'V1']:
        chordmap(INPUT_FILE, True)
    elif choice in ['v2', 'V2']:
        chordmap_2(INPUT_FILE, True)
    else:
        choice3 = input("Test chordmap()? [v1/v2/n]: ")
        if choice3 in ['v1', 'V1']:
            chordmap(INPUT_FILE, False)
        elif choice3 in ['v2', 'V2']:
            chordmap_2(INPUT_FILE, False)

    choice2 = input("Enter real-time MIDI-ANN input mode? ")
    if choice2 in ['y', 'Y']:
        realTimeMIDIChords()
