'''
MOIRA
Mediating Output Interpreter for Real-time Analysis
version 1.0
author: R2-B09, 2018

An algorithm that shows the chord name
for every combination of neural network outputs.
'''

import math
import numpy as NP

UPPER_BOUNDS = [0.08, 0.16, 0.24, 0.32, 0.40, 0.48, 0.56, 0.64, 0.72, 0.80, 0.88, 0.96]
NOTES        = ['C',  'C#', 'D',  'D#', 'E',  'F',  'F#', 'G',  'G#', 'A',  'A#', 'B']

def softmax(x, verbose=False):
    x_exp = [math.exp(i) for i in x]
    #print([round(i, 2) for i in x_exp])
    sum_x_exp = sum(x_exp)
    #print(round(sum_x_exp, 2))
    soft_max = [round(i / sum_x_exp, 3) for i in x_exp]
    if verbose:
        print(soft_max)
    return soft_max

def determineNote(NEURON_0_VALUE):
    #print(NEURON_0_VALUE)
    if NEURON_0_VALUE < 0.08:
        return 'C'
    else:
        for i in range(1, 12):
            if UPPER_BOUNDS[i - 1] < NEURON_0_VALUE <= UPPER_BOUNDS[i]:
                return NOTES[i]
            elif NEURON_0_VALUE >= 0.96:
                return "B"

def determineChordName(outputs, inputs, verbose=False) -> str:

    # Access the expected outputs for the inputs
    possible_expected_outputs = NP.load("input_dataset/samples/database/NP_ALL_EXPECTED_OUTPUTS.npy")
    possible_expected_inputs = NP.load("input_dataset/samples/database/NP_ALL_EXPECTED_INPUTS.npy")
    comparator_of_expected_inputs_index = -1
    ips = NP.array(inputs)

    if verbose:
        print("possible_expected_inputs: " + str(possible_expected_inputs))

    # Check which index of inputs corresponds to the given inputs
    for i in range(len(possible_expected_inputs)):
        if possible_expected_inputs[i][0] == ips[0]:
            if NP.array_equal(possible_expected_inputs[i], ips):
                comparator_of_expected_inputs_index = i
                break

    # Access the corresponding outputs
    expected_outputs = possible_expected_outputs[comparator_of_expected_inputs_index]
    if verbose:
        print(expected_outputs)

    # Main determine chord name routine
    rn = float(outputs[0])
    softmax_in = []
    for i in range(1, len(expected_outputs)):
        softmax_in.append(expected_outputs[i])
    ROOT_NOTE = determineNote(rn)
    if verbose:
        print(ROOT_NOTE)
    chord_modifiers = ""

    soft_max_expected = [0]
    soft_max_expected.extend(softmax(softmax_in, verbose))

    for output_neuron in range(1, len(outputs)):
        if outputs[output_neuron] >= soft_max_expected[output_neuron]:             # The number contained is 1
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
        if outputs[output_neuron] >= soft_max_expected[output_neuron]:
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
        if outputs[output_neuron] >= soft_max_expected[output_neuron]:
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
def test__():
    # the_road = input("Enter the chord output: ").strip().split(' ')
    # #print(cs)
    # c = []
    # for k in the_road:
    #     if len(k) > 1:
    #         c.append(float(k))
    #     else:
    #         c.append(int(k))
    #print(c)

    #      n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
    # Expected: A#11sus2
    c = [0.09, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    print(determineChordName(c))

# TESTER BLOCK
# if __name__ == "__main__":
#     test__()
