'''
MOIRA
Mediating Output Interpreter for Real-time Analysis
version 1.0
author: R2-B09, 2018

An algorithm that shows the chord name
for every combination of neural network outputs.
'''

UPPER_BOUNDS = [0.08, 0.16, 0.24, 0.32, 0.40, 0.48, 0.56, 0.64, 0.72, 0.80, 0.88, 0.96]
NOTES        = ['C',  'C#', 'D',  'D#', 'E',  'F',  'F#', 'G',  'G#', 'A',  'A#', 'B']

def determineNote(NEURON_0_VALUE):
    if NEURON_0_VALUE < 0.08:
        return None
    else:
        for i in range(1, 12):
            if UPPER_BOUNDS[i - 1] <= NEURON_0_VALUE < UPPER_BOUNDS[i]:
                return NOTES[i - 1]
            elif NEURON_0_VALUE >= 0.96:
                return "B"

def determineChordName(outputs):
    rn = float(outputs[0])
    ROOT_NOTE = determineNote(rn)
    chord_modifiers = ""

    for output_neuron in range(1, len(outputs)):
        if outputs[output_neuron] == 1:             # The number contained is 1
            if output_neuron == 1:                  # The index is some value
                chord_modifiers += "maj"
            elif output_neuron == 2:
                chord_modifiers += "min"
            elif output_neuron == 7 and outputs[2] == 1 and outputs[9] == 1:
                chord_modifiers += "o"
            elif output_neuron == 3:
                chord_modifiers += "aug"
            elif output_neuron == 4:
                chord_modifiers += "dim"
            else:
                pass

    for output_neuron in range(1, len(outputs)):
        if outputs[output_neuron] == 1:
            if output_neuron == 8:
                chord_modifiers += "6"
            elif output_neuron == 9:
                chord_modifiers += "7"
            elif output_neuron == 10:
                chord_modifiers += "9"
            elif output_neuron == 11:
                chord_modifiers += "11"
            elif output_neuron == 12:
                chord_modifiers += "maj7"
            else:
                pass

    for output_neuron in range(1, len(outputs)):
        if outputs[output_neuron] == 1:
            if output_neuron == 13:
                chord_modifiers += "(9)"
            elif output_neuron == 5:
                chord_modifiers += "sus2"
            elif output_neuron == 6:
                chord_modifiers += "sus4"
            elif output_neuron == 7 and outputs[2] == 1 and outputs[9] == 1:
                chord_modifiers = "o7"
            else:
                pass

    return ROOT_NOTE + chord_modifiers

# Tester
def test():
    the_road = input("Enter the chord output: ").strip().split(' ')
    #print(cs)
    c = []
    for k in the_road:
        if len(k) > 1:
            c.append(float(k))
        else:
            c.append(int(k))
    #print(c)

    #       n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
    #c = [0.88, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    print(determineChordName(c))

# TESTER BLOCK
# if __name__ == "__main__":
#     test()
