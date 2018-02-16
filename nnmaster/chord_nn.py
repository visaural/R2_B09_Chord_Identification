'''
chord_nn.py
version 0.1
author: R2_B09
'''

#from keras.models import Sequential
#from keras.layers import Input, Dense
#import keras.callbacks
import numpy as NP
import h5py

INPUT_VALS = NP.load("input_dataset/samples/database/NP_INPUT_NEURON_VALUES.npy")
OUTPUT_VALS = NP.load("input_dataset/samples/database/NP_OUTPUT_NEURON_VALUES.npy")
VALIDATION_INPUT_VALS = NP.load("input_dataset/samples/database/NP_INPUT_NEURON_VALUES_NOT_SAMPLE.npy")
VALIDATION_OUTPUT_VALS = NP.load("input_dataset/samples/database/NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE.npy")

def splitter():
    # VALIDATION_I = NP.array_split(VALIDATION_INPUT_VALS, 2)
    # VALIDATION_O = NP.array_split(VALIDATION_OUTPUT_VALS, 2)
    #
    # # VALIDATION_I = []
    # # VALIDATION_O = []
    # #
    # # for i in range(INPUT_VALS.size):
    #
    #
    # NP.save("input_dataset/samples/database/NP_INPUT_VALIDATION.npy", VALIDATION_I[0])
    # NP.save("input_dataset/samples/database/NP_INPUT_TEST.npy", VALIDATION_I[1])
    # NP.save("input_dataset/samples/database/NP_OUTPUT_VALIDATION.npy", VALIDATION_O[0])
    # NP.save("input_dataset/samples/database/NP_OUTPUT_TEST.npy", VALIDATION_O[1])

    VI = VALIDATION_INPUT_VALS.tolist()
    VO = VALIDATION_OUTPUT_VALS.tolist()
    print(VI, len(VI))
    print(VO, len(VO))

    VI_TEST = []
    VO_TEST = []
    VI_VALI = []
    VO_VALI = []

    for i in range(len(VI)):
        if i % 2 == 0:
            VI_VALI.append(VI[i])
            VO_VALI.append(VO[i])
        else:
            VI_TEST.append(VI[i])
            VO_TEST.append(VO[i])

    NP.save("input_dataset/samples/database/NP_INPUT_VALIDATION.npy", NP.array(VI_VALI))
    NP.save("input_dataset/samples/database/NP_INPUT_TEST.npy", NP.array(VI_TEST))
    NP.save("input_dataset/samples/database/NP_OUTPUT_VALIDATION.npy", NP.array(VO_VALI))
    NP.save("input_dataset/samples/database/NP_OUTPUT_TEST.npy", NP.array(VO_TEST))





splitter()


#chord_identifier = Sequential()
