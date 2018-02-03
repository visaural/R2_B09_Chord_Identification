'''
chord_nn.py
version 0.1
author: R2_B09
'''

import keras
import numpy as NP
import h5py

INPUT_VALS = NP.load("samples/database/NP_INPUT_NEURON_VALUES.npy")
OUTPUT_VALS = NP.load("samples/database/NP_OUTPUT_NEURON_VALUES.npy")