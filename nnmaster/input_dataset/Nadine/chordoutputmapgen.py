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
SPACE_LENGTH = 10

def chordmap_2_write(in_file = '../input_dataset_binaries_2.txt', out_file = "../input_dataset_output_binaries_2.txt"):
    with open(in_file, 'r') as fi:
        rawListChordFile = [i.strip().split() for i in fi]
        print(rawListChordFile[0])

        inputs = []
        outputs = []

        for c in range(len(rawListChordFile)):
            inputs.append([])
            for k in range(1, len(rawListChordFile[c])):
                inputs[c].append(rawListChordFile[c][k])

        print(inputs[0])

        for d in range(len(rawListChordFile)):
            outputs.append(list_1_at_index(chord_number(rawListChordFile[d][0])))

        print(outputs[0])
        print(len(outputs[0]))

        # Write to file
        with open(out_file, 'w') as fo:
            for chord_instance in range(len(inputs)):
                fo.write(rawListChordFile[chord_instance][0] + (" " * (SPACE_LENGTH - len(rawListChordFile[chord_instance][0]))))
                for note_binary in range(len(outputs[chord_instance])):
                    fo.write(str(outputs[chord_instance][note_binary]) + " ")
                fo.write("\n")

def list_1_at_index(i, size = 444):
    '''
    Returns a list with a 1 at index i.
    :return:
    '''
    l = []
    for k in range(size):
        if k == i:
            l.append(1)
        else:
            l.append(0)
    return l

def chord_number(chord_string):
    '''
    Returns the order of the chord in the chord list.
    :param chord_string:
    :return: The chord order, given by 37N + S
    '''

    if chord_string[:2] in ['C#', 'D#', 'F#', 'G#', 'A#']:
        root_note_string = chord_string[:2]
        chord_type_string = chord_string[2:]
    else:
        root_note_string = chord_string[:1]
        chord_type_string = chord_string[1:]
    #print(root_note_string)
    #print(chord_type_string)
    root_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    chord_types = ['maj', 'min', 'aug', 'dim', 'sus2', 'sus4', 'M7', 'm7', '7', 'aug7', 'dim7', 'o7', 'M7sus2', 'M7sus4', '7sus2', '7sus4', 'M9', 'm9', '9', 'aug9', 'dim9', 'M9sus2', 'M9sus4', '9sus2', '9sus4', 'M11', 'm11', '11', 'aug11', 'M11sus2', '11sus2', 'mM7', 'mM7(9)', 'M6', 'm6', 'M6(9)', 'm6(9)']

    root_note_index = root_notes.index(root_note_string)
    chord_type_index = chord_types.index(chord_type_string)

    return ((37 * root_note_index) + chord_type_index)


def chordmap(N, CT):
    i = 0
    while i < len(N):
        for chord in CT:
            chordTypeNeurons = []
            # chord[0] = N[i]
            # listOfOutputVectors.append(chord)
            listOfOutputVectors.append((N[i], chord[1], chord[2], chord[3], chord[4], chord[5], chord[6], chord[7], chord[8], chord[9], chord[10], chord[11], chord[12], chord[13]))
            #for k in range(1, len(chord)):
            #    chordTypeNeurons.append(chord[k])
            #listOfOutputVectors.append((N[i]))
            #listOfOutputVectors.append((N[i], [j for j in chordTypeNeurons]))
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
    #chordmap(NOTES, CHORD_TYPES)
    #writeToFile(listOfOutputVectors)
    chordmap_2_write('../input_dataset_binaries_2.txt')