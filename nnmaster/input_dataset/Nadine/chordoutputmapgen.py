'''
NADINE
Neural Array Dataset Interpreter for Note Extrapolates
version 1.1
author: R2-B09, 2017

Converts chord input file to data that can be interpreted by the ANN.
'''

'''
output_mappings.py
Mappings of chord types to NN outputs.
'''

import output_mappings

NOTES = [0.08, 0.16, 0.24, 0.32, 0.40, 0.48, 0.56, 0.64, 0.72, 0.80, 0.88, 0.96]
CHORD_TYPES = [
    output_mappings.MAJOR,
    output_mappings.MINOR,
    output_mappings.AUGMENTED,
    output_mappings.DIMINISHED,
    output_mappings.SUS2,
    output_mappings.SUS4,

    output_mappings.MAJOR_7,
    output_mappings.MINOR_7,
    output_mappings.DOMINANT_7,
    output_mappings.AUG_7,
    output_mappings.DIM_7,
    output_mappings.HALF_DIM,
    output_mappings.MAJOR_7_SUS2,
    output_mappings.MAJOR_7_SUS4,
    output_mappings.DOM_7_SUS2,
    output_mappings.DOM_7_SUS4,

    output_mappings.MAJOR_9,
    output_mappings.MINOR_9,
    output_mappings.DOMINANT_9,
    output_mappings.AUG_9,
    output_mappings.DIM_9,
    output_mappings.MAJOR_9_SUS2,
    output_mappings.MAJOR_9_SUS4,
    output_mappings.DOM_9_SUS2,
    output_mappings.DOM_9_SUS4,

    output_mappings.MAJOR_11,
    output_mappings.MINOR_11,
    output_mappings.DOMINANT_11,
    output_mappings.AUG_11,
    output_mappings.MAJOR_11_SUS2,
    output_mappings.DOM_11_SUS2,

    output_mappings.MIN_MAJ_7,
    output_mappings.MIN_MAJ_7_9,
    output_mappings.MAJ_6,
    output_mappings.MIN_6,
    output_mappings.MAJ_6_9,
    output_mappings.MIN_6_9,
]

INPUT_FILE = "../input_dataset.txt"
OUTPUT_FILE = "../input_dataset_output_binaries.txt"
listOfOutputVectors = []

def chordmap(N, CT):
    i = 0
    while i < len(N):
        for chord in CT:
            # chord[0] = N[i]
            # listOfOutputVectors.append(chord)
            listOfOutputVectors.append((N[i], chord[1], chord[2], chord[3], chord[4], chord[5], chord[6], chord[7], chord[8], chord[9], chord[10], chord[11], chord[12], chord[13]))
        i += 1

    for i in listOfOutputVectors: print(i)
    print(len(listOfOutputVectors))

def writeToFile(LOOV):
    SPACE_LENGTH = 10
    f = open(INPUT_FILE)
    rawListChordFile = [i.strip().split() for i in f]

    for i in range(4):
        rawListChordFile.pop()

    chordsList = [rawListChordFile[i][0] for i in range(len(rawListChordFile))]

    try:
        with open(OUTPUT_FILE, 'w') as of:
            of.write("CHORD      note  ma mi au di s2 s4 b5 ~6 ~7 ~9 11 +M7 +9\n")
            for i in range(len(chordsList)):
                of.write(chordsList[i] + ((SPACE_LENGTH - len(chordsList[i])) * " "))
                of.write(str(LOOV[i]))
                of.write("\n")
    except Exception as e:
        print(e)

    print("File write complete.")


if __name__ == "__main__":
    chordmap(NOTES, CHORD_TYPES)
    writeToFile(listOfOutputVectors)