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


# Notes
C               = 0.08
C_SHARP         = 0.16
D               = 0.24
D_SHARP         = 0.32
E               = 0.40
F               = 0.48
F_SHARP         = 0.56
G               = 0.64
G_SHARP         = 0.72
A               = 0.80
A_SHARP         = 0.88
B               = 0.96
# Triads
#                  n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
MAJOR           = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MINOR           = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AUGMENTED       = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DIMINISHED      = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SUS2            = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
SUS4            = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 7-based
#                  n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
MAJOR_7         = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
MINOR_7         = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
DOMINANT_7      = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
AUG_7           = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
DIM_7           = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
HALF_DIM        = [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
MAJOR_7_SUS2    = [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
MAJOR_7_SUS4    = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
DOM_7_SUS2      = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
DOM_7_SUS4      = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
# 9-based
#                  n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
MAJOR_9         = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
MINOR_9         = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
DOMINANT_9      = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
AUG_9           = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
DIM_9           = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
MAJOR_9_SUS2    = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
MAJOR_9_SUS4    = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
DOM_9_SUS2      = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
DOM_9_SUS4      = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
# 11-based
#                  n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
MAJOR_11        = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
MINOR_11        = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
DOMINANT_11     = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
AUG_11          = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
MAJOR_11_SUS2   = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
DOM_11_SUS2     = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

# Special
#                  n  ma mi a  d  s2 s4 b5 6  7  9  11 +M7+9
MIN_MAJ_7       = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
MIN_MAJ_7_9     = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
MAJ_6           = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
MIN_6           = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
MAJ_6_9         = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
MIN_6_9         = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
