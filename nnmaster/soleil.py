'''
SOLEIL
Summative Output Landscaper of Errors, Inconsistencies, and Latencies
version 2.0
author: R2-B09, 2018

Various methods for recording the value of the cost function.
'''

import matplotlib.pyplot as plt

def graph_from_History(things_to_graph, MHObject, title=None, ylabel=None, xlabel=None, legendlist=None, legendloc='upper left'):
    for i in range(len(things_to_graph)):
        plt.plot(MHObject.history[things_to_graph[i]])

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(legendlist, loc=legendloc)
    plt.show()
