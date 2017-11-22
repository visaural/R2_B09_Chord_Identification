#### /nnmaster/input_dataset
## THE INPUT DATASET

#### `/Dianne`: _Dataset Initiation Algorithm for Nominal Note Extrapolation_
Sets up the chords to be used as input to the ANN.
Output: `input_dataset.txt`
#### `/Nadine`: _Neural Array Dataset Interpreter for Note Extrapolates_ 
Converts the chords to a form that can be interpreted by the ANN.
Specifically, `Nadine` converts each input chord to 2 vectors:
1. A 24-magnitude input vector (`input_dataset_binaries.txt`)
2. A 14-magnitude output vector (`input_dataset_output_binaries.txt`)

#### `/samples`: Training and evaluation samples.
