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
            elif NEURON_0_VALUE > 0.96:
                return "B"
            else:
                return None

# Tester
if __name__ == "__main__":
    print(determineNote(0.95))
