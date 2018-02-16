'''
chord_nn_tester.py
version 0.1
author: R2_B09
'''
import sys
import keras
import numpy as NP
import h5py
import loc_note_MIDI
import pygame
from pygame import midi
from pygame.locals import *
import moira as moi
import soleil as sol

def check_gpu():
    from keras import backend as K
    K.tensorflow_backend._get_available_gpus()

def NNtest(INPUT, EXPECTED_OUTPUT):
    '''
    Runs a single NN test pass given input and expected outs as numpy arrays.
    :param EXPECTED_INPUT: Numpy array for expected input.
    :param EXPECTED_OUTPUT: Numpy array for expected output.
    :return:
    '''
    # TODO: ADD NN (TEST FOR INDIVIDUAL SAMPLE) CODE HERE

    # SAFETY NET: If nothing is running through realtime input then pass
    if INPUT is None or len(INPUT) < 24:
        pass
    else:
        # TODO: Add NN code here
        pass

def realTimeTest():
    '''
    Displays the mappings of the notes currently being played on MIDI and runs them through the NN,
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

            # TODO: FILL PARAMETERS FOR NNtest()
            NNtest(currentNotesInChord, [])

    print("Exiting.")
    midi_in.close()
    pygame.midi.quit()
    pygame.quit()
    exit()


# if __name__ == "__main__":
#     check_gpu()