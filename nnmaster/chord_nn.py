'''
chord_nn.py
version 0.1
author: R2_B09
'''

from keras.models import Sequential, load_model
from keras.layers import Dense
import keras.callbacks
import numpy as NP
import h5py
import soleil as sol

FIRST_RUN = True

INPUT_VALS = NP.load("input_dataset/samples/database/NP_INPUT_NEURON_VALUES.npy")
OUTPUT_VALS = NP.load("input_dataset/samples/database/NP_OUTPUT_NEURON_VALUES.npy")
VALIDATION_INPUT_VALS = NP.load("input_dataset/samples/database/NP_INPUT_NEURON_VALUES_NOT_SAMPLE.npy")
VALIDATION_OUTPUT_VALS = NP.load("input_dataset/samples/database/NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE.npy")


def splitter():

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

def save_history(mh):

    MODE = 'w' if FIRST_RUN else 'a'

    with open("models/history/mse.txt", MODE) as ModelHistoryMSE:
         ModelHistoryMSE.write(str(mh.history['mean_squared_error']))

    with open("models/history/val_acc.txt", MODE) as ModelHistoryVA:
        ModelHistoryVA.write(str(mh.history['val_acc']))

    with open("models/history/val_loss.txt", MODE) as ModelHistoryVL:
        ModelHistoryVL.write(str(mh.history['val_loss']))


if __name__ == "__main__":


    if FIRST_RUN:
        chord_identifier = Sequential()
        chord_identifier.add(Dense(14, input_shape = (24,), activation = 'sigmoid'))
        chord_identifier.add(Dense(2))
        chord_identifier.add(Dense(2))
        chord_identifier.add(Dense(14, activation = 'softmax'))

        chord_identifier.compile(optimizer = 'sgd', loss = 'mean_squared_error', metrics = ['mse', 'accuracy'])
        checkpointer = keras.callbacks.ModelCheckpoint("models/chord_identifier.h5", verbose=1)

        h = chord_identifier.fit(INPUT_VALS, OUTPUT_VALS, epochs = 1000, verbose = 1, validation_data = (VALIDATION_INPUT_VALS, VALIDATION_OUTPUT_VALS))
        save_history(h)

        sol.graph_from_History(things_to_graph=['acc', 'val_acc'], MHObject=h, title="Model accuracy", ylabel="Accuracy", xlabel="Epoch", legendlist=['train', 'test'], legendloc = 'upper left')
        sol.graph_from_History(things_to_graph=['loss', 'val_loss'], MHObject=h, title="Model losses", ylabel="Loss", xlabel="Epoch", legendlist=['train', 'test'], legendloc = 'upper left')

    else:
        # recall and train
        chord_identifier = keras.models.load_model("models/chord_identifier.h5")
        chord_identifier.compile(optimizer='sgd', loss='mean_squared_error', metrics=['mse', 'accuracy'])
        checkpointer = keras.callbacks.ModelCheckpoint("models/chord_identifier.h5", verbose=1)

        h = chord_identifier.fit(INPUT_VALS, OUTPUT_VALS, epochs=1000, verbose=1, validation_data=(VALIDATION_INPUT_VALS, VALIDATION_OUTPUT_VALS))
        save_history(h)

        sol.graph_from_History(things_to_graph=['acc', 'val_acc'], MHObject=h, title="Model accuracy", ylabel="Accuracy", xlabel="Epoch", legendlist=['train', 'test'], legendloc = 'upper left')
