import numpy

m = "__main__"

if __name__ == m:


    x = numpy.load("NP_INPUT_NEURON_VALUES.npy")
    print(x)
    print(x.size)

    x = numpy.load("NP_OUTPUT_NEURON_VALUES.npy")
    print(x)
    print(x.size)

    x = numpy.load("NP_INPUT_NEURON_VALUES_NOT_SAMPLE.npy")
    print("ORIGINAL INPUT")
    print(x)
    print(x[0].size)

    x = numpy.load("NP_OUTPUT_NEURON_VALUES_NOT_SAMPLE.npy")
    print("ORIGINAL OUTPUT")
    print(x)
    print(x.size)

    x = numpy.load("NP_INPUT_VALIDATION.npy")
    print("INPUT VALIDATION")
    print(x)
    print(x.size)
    x = numpy.load("NP_OUTPUT_VALIDATION.npy")
    print("OUTPUT VALIDATION")
    print(x)
    print(x.size)

    x = numpy.load("NP_INPUT_TEST.npy")
    print("INPUT TEST")
    print(x)
    print(x.size)
    x = numpy.load("NP_OUTPUT_TEST.npy")
    print("OUTPUT TEST")
    print(x)
    print(x.size)

    print(type(x[2][3]))

