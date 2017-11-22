'''
kushalbhabra: midi_test
with functions from:
    Stephen Tang (stephentang.io)
'''

'''
Citations:
kushalbhabra (2013). pyMidi [GitHub repository]. Retrieved November 17, 2017, from 
    https://github.com/kushalbhabra/pyMidi.

Tang, S. (n.d.) Python code raw data from a MIDI controller. Retrieved from 
    http://www.stephentang.io/python-code-raw-data-from-a-midi-controller/
'''

import pygame
import pygame.midi
from pygame.locals import *
from giantwin32 import *


# display a list of MIDI devices connected to the computer
# this function written by Stephen Tang, stephentang.io
def print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r
        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"
        print ("%2i: interface: %s, name: %s, opened: %s %s" %
               (i, interf, name, opened, in_out))


pygame.init()

pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()

print("Available MIDI devices:")
print_device_info()

MI = int(input("Select device ID: ")) # 2 the default for Project-X99

'''
INPUT 2: Komplete Kontrol 1
INPUT 3: Komplete Kontrol EXT
INPUT 4: Komplete Kontrol DAW
'''

input_id = MI
i = pygame.midi.Input(input_id)

pygame.display.set_caption("midi test")
screen = pygame.display.set_mode((400, 300), RESIZABLE, 32)

print("starting")

going = True

while going:

    events = event_get()
    for e in events:
        if e.type in [QUIT]:
            going = False
        if e.type in [KEYDOWN]:
            going = False

    if i.poll():
        # print("MIDI event exists.")
        midi_events = i.read(10)
        print(midi_events)
        # if int(midi_events[0][0][0]) in [224, 225, 226]:  # Pitch Bender
        #     print(str(midi_events[0][0][2]))  # right(0)  center(64)  left(124)
        #
        #     # print "full midi_events " + str(midi_events)
        #     # print "my midi note is " + str(midi_events[0][0][1])
        # # convert them into pygame events.
        # midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
        #
        # for m_e in midi_evs:
        #     event_post(m_e)

print("exit button clicked.")
i.close()
pygame.midi.quit()
pygame.quit()
exit()
"""
reads num_events midi events from the buffer.
Input.read(num_events): return midi_event_list
Reads from the Input buffer and gives back midi events. [[[status,data1,data2,data3],timestamp],
 [[status,data1,data2,data3],timestamp],...]
"""
