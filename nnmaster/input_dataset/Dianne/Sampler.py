'''
DIANNE
Dataset Initiation Algorithm for Nominal Note Extrapolation
version 1.3
author: Joachim Navarro, 2017

Zeroth-inversion-chord input dataset generator for use in neural networks.
'''

'''
Sampler.py
Stratified random sampler.
'''

import scale
import chord
import ChordTypes
import random
import numpy as NP

listOfChordsOfChordTypes = []
listOfChords = []
sampleChords = []
flatSampleChords = []
notInTheSample = []
ct = []
SAMPLE_SIZE_G = 7
INPUTS = "../input_dataset_binaries.txt"
OUTPUTS = "../input_dataset_output_binaries.txt"
SAMPLE_FILE = "../samples/sample_one.txt"


def chordgen():
    for rootNote in scale.TWELVE_NOTE_SCALE:
        for chordType in scale.CHORD_TYPES:
            listOfChords.append(chord.Chord(rootNote, chordType))

    print(listOfChords)

def output_array_to_file(in_sample, out_sample, in_notsample, out_notsample):
    IS_FP = "../samples/database/NP_INPUT_NEURON_VALUES.npy"
    OS_FP = "../samples/database/NP_OUTPUT_NEURON_VALUES.npy"
    INS_FP = "../samples/database/NP_INPUT_NEURON_VALUES_NOT_SAMPLE.npy"
    ONS_FP = "../samples/database/NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE.npy"

    NP.save(IS_FP, in_sample)
    NP.save(OS_FP, out_sample)
    NP.save(INS_FP, in_notsample)
    NP.save(ONS_FP, out_notsample)

    print("numpy array save complete.")


def sample(SAMPLE_SIZE):
    # Makes list of list of chords. The top level list is broken down into lists of chords grouped by type
    for type in range(0, ChordTypes.NUMBER_OF_CHORD_TYPES):
        listOfChordsOfChordTypes.append([])
        for chord in range(0, ChordTypes.NUMBER_OF_CHORDS, ChordTypes.NUMBER_OF_CHORD_TYPES):
            listOfChordsOfChordTypes[type].append(listOfChords[chord + type])

    print(listOfChordsOfChordTypes)
    print(len(listOfChordsOfChordTypes))

    for ctListIndex in range(len(listOfChordsOfChordTypes)):
        #for r in range(SAMPLE_SIZE):
        sampleChords.append(random.sample(listOfChordsOfChordTypes[ctListIndex], SAMPLE_SIZE))

    flatSampleChords = [_chord_ for _chordList_ in sampleChords for _chord_ in _chordList_]

    for c in listOfChords:
        if c not in flatSampleChords:
            notInTheSample.append(c)

    print("sample chords:", sampleChords)
    print("flat list:", flatSampleChords)
    print("not in the sample:", notInTheSample)
    printEqualElements(flatSampleChords, notInTheSample)

    print("Sample size:", str(len(flatSampleChords)), "(" , str(ChordTypes.NUMBER_OF_CHORD_TYPES), "chord types *", SAMPLE_SIZE, "chords per type)")

    print(4 * '\n')

    # ===============================================================================
    # WRITING SUBROUTINE

    inputs_file = open(INPUTS, 'r')
    outputs_file = open(OUTPUTS, 'r')
    inputs_file_contents = [i.strip().split() for i in inputs_file]
    outputs_file_contents = [i.strip().split() for i in outputs_file]

    INPUT_NEURON_VALUES = []
    OUTPUT_NEURON_VALUES = []
    INPUT_NEURON_VALUES_NOT_SAMPLE = []
    OUTPUT_NEURON_VALUES_NOT_SAMPLE = []

    temp1 = []
    temp2 = []

    print(inputs_file_contents)
    print(len(inputs_file_contents))
    print(outputs_file_contents)
    print(len(outputs_file_contents))
    print()

    with open(SAMPLE_FILE, 'w') as sampleFile:
        counter = 0
        print(len(flatSampleChords))
        for sampleChord in range(len(flatSampleChords)):

            for inputs_index in range(len(inputs_file_contents)):
                # print(inputs_file_contents[inputs_index][0])
                # print(flatSampleChords[sampleChord].__repr__())
                if inputs_file_contents[inputs_index][0] == flatSampleChords[sampleChord].__repr__():
                    counter += 1
                    print(counter)

                    # Name of the chord
                    print(flatSampleChords[sampleChord], end=" ")
                    sampleFile.write(flatSampleChords[sampleChord].__repr__() + " ")

                    # Input representation of the chord as a 24-number list
                    print("INPUTS:", end=" ")
                    sampleFile.write("INPUTS: ")

                    for i in range(1, len(inputs_file_contents[inputs_index])):
                        # Print the value for bug fixing
                        print(inputs_file_contents[inputs_index][i], end=" ")
                        # Append the value to be written to the file to the numpy array
                        temp1.append(inputs_file_contents[inputs_index][i])
                        # Write the value to the file
                        sampleFile.write(inputs_file_contents[inputs_index][i] + " ")

                    INPUT_NEURON_VALUES.append(temp1)
                    temp1 = []

                    # Output representation of the chord as a 14-number list
                    print("OUTPUTS:", end=" ")
                    sampleFile.write("OUTPUTS: ")

                    for k in range(1, len(outputs_file_contents[inputs_index])):
                        # Print the value for bug fixing
                        print(outputs_file_contents[inputs_index][k], end=" ")
                        # Append the value to be written to the file to the numpy array
                        temp2.append(outputs_file_contents[inputs_index][k])
                        # Write the value to the file
                        sampleFile.write(outputs_file_contents[inputs_index][k] + " ")

                    OUTPUT_NEURON_VALUES.append(temp2)
                    temp2 = []

                    print()
                    sampleFile.write("\n")

        print("\nNOT IN THE SAMPLE\n")
        sampleFile.write("\nNOT IN THE SAMPLE\n")
        for sampleChord in range(len(notInTheSample)):
            for inputs_index in range(len(inputs_file_contents)):
                # print(inputs_file_contents[inputs_index][0])
                # print(flatSampleChords[sampleChord].__repr__())
                if inputs_file_contents[inputs_index][0] == notInTheSample[sampleChord].__repr__():
                    counter += 1
                    print(counter)

                    print(notInTheSample[sampleChord], end=" ")
                    sampleFile.write(notInTheSample[sampleChord].__repr__() + " ")

                    print("INPUTS:", end=" ")
                    sampleFile.write("INPUTS: ")

                    for i in range(1, len(inputs_file_contents[inputs_index])):
                        print(inputs_file_contents[inputs_index][i], end=" ")
                        # Append the value to be written to the file to the numpy array
                        temp1.append(inputs_file_contents[inputs_index][i])
                        sampleFile.write(inputs_file_contents[inputs_index][i] + " ")

                    INPUT_NEURON_VALUES_NOT_SAMPLE.append(temp1)
                    temp1 = []

                    print("OUTPUTS:", end=" ")
                    sampleFile.write("OUTPUTS: ")

                    for k in range(1, len(outputs_file_contents[inputs_index])):
                        print(outputs_file_contents[inputs_index][k], end=" ")
                        # Append the value to be written to the file to the numpy array
                        temp2.append(outputs_file_contents[inputs_index][k])
                        sampleFile.write(outputs_file_contents[inputs_index][k] + " ")

                    OUTPUT_NEURON_VALUES_NOT_SAMPLE.append(temp2)
                    temp2 = []

                    print()
                    sampleFile.write("\n")

        # print(INPUT_NEURON_VALUES)
        # print(OUTPUT_NEURON_VALUES)
        # print(INPUT_NEURON_VALUES_NOT_SAMPLE)
        # print(OUTPUT_NEURON_VALUES_NOT_SAMPLE)

        # Make numpy arrays of the sample

        NP_INPUT_NEURON_VALUES = NP.array(INPUT_NEURON_VALUES)
        NP_OUTPUT_NEURON_VALUES = NP.array(OUTPUT_NEURON_VALUES)
        NP_INPUT_NEURON_VALUES_NOT_SAMPLE = NP.array(INPUT_NEURON_VALUES_NOT_SAMPLE)
        NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE = NP.array(OUTPUT_NEURON_VALUES_NOT_SAMPLE)

        print("-------------------------------------")
        print("NUMPY ARRAYS")
        print("-------------------------------------")
        print()
        print("NP_INPUT_NEURON_VALUES")
        print(NP_INPUT_NEURON_VALUES)
        print()
        print("NP_OUTPUT_NEURON_VALUES")
        print(NP_OUTPUT_NEURON_VALUES)
        print()
        print("NP_INPUT_NEURON_VALUES_NOT_SAMPLE")
        print(NP_INPUT_NEURON_VALUES_NOT_SAMPLE)
        print()
        print("NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE")
        print(NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE)
        print("-------------------------------------")

        # Outputs sample arrays to h5
        output_array_to_file(NP_INPUT_NEURON_VALUES, NP_OUTPUT_NEURON_VALUES, NP_INPUT_NEURON_VALUES_NOT_SAMPLE, NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE)


def anyTwoElementsEqual(CBL, CL):
    for i in range(len(CBL)):
        for j in range(i + 1, len(CBL)):
            if CBL[i] == CBL[j]:
                print(CL[i][0], "and", CL[j][0])
                return True

    return False

def printEqualElements(CBL, CL):

    if not anyTwoElementsEqual(CBL, CL):
        print("No elements of the two lists are the same.")
    else:
        ee = []
        for i in range(len(CBL)):
            for j in range(i + 1, len(CBL)):
                if CBL[i] == CBL[j]:
                    print(CL[i][0], "and", CL[j][0])
                    ee.append(CL[i][0])
                    ee.append(CL[j][0])

        print(len(ee) // 2)


# =============== MAIN THREAD ===============

chordgen()

if SAMPLE_SIZE_G < 12:
    sample(SAMPLE_SIZE_G)
    #writeSampleToFile(flatSampleChords, notInTheSample)
else:
    print("Sample invalid.")
