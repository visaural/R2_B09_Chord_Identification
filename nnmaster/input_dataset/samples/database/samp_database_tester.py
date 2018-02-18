import numpy

m = "__main__"

def merge():
    o1 = numpy.load("NP_OUTPUT_NEURON_VALUES.npy").astype(float)
    o2 = numpy.load("NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE.npy").astype(float)
    i1 = numpy.load("NP_INPUT_NEURON_VALUES.npy").astype(float)
    i2 = numpy.load("NP_INPUT_NEURON_VALUES_NOT_SAMPLE.npy").astype(float)

    o_all = numpy.concatenate((o1, o2))
    i_all = numpy.concatenate((i1, i2))

    print(i_all)
    print(o_all)

    numpy.save("NP_ALL_EXPECTED_OUTPUTS.npy", o_all)
    numpy.save("NP_ALL_EXPECTED_INPUTS.npy", i_all)

if __name__ == m:
    merge()

    # x = numpy.load("NP_INPUT_NEURON_VALUES.npy")
    # print(x)
    # print(x.size)
    #
    # x = numpy.load("NP_OUTPUT_NEURON_VALUES.npy")
    # print(x)
    # print(x.size)
    #
    # x = numpy.load("NP_INPUT_NEURON_VALUES_NOT_SAMPLE.npy")
    # print("ORIGINAL INPUT")
    # print(x)
    # print(x[0].size)
    #
    # x = numpy.load("NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE.npy")
    # print("ORIGINAL OUTPUT")
    # print(x)
    # print(x.size)
    #
    # x = numpy.load("NP_INPUT_VALIDATION.npy")
    # print("INPUT VALIDATION")
    # print(x)
    # print(x.size)
    # x = numpy.load("NP_OUTPUT_VALIDATION.npy")
    # print("OUTPUT VALIDATION")
    # print(x)
    # print(x.size)
    #
    # x = numpy.load("NP_INPUT_TEST.npy")
    # print("INPUT TEST")
    # print(x)
    # print(x.size)
    # x = numpy.load("NP_OUTPUT_TEST.npy")
    # print("OUTPUT TEST")
    # print(x)
    # print(x.size)
    #
    # print(type(x[2][3]))

