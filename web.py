import networkx as nx
from Markov import Markov_process
import numpy as np

class web_surfer(Markov_process):
    """ simulates someone having fun clicking on random internet links / nodes.
    Takes internet digraph as input.
    Produces corresponding Google transition matrix for sake of Markov_process """
    def __init__(self, I_graph, alpha=.85):
        G = nx.google_matrix(I_graph)
        # key to make indexing consistent
        G = np.array(G)
        Markov_process.__init__(self, I_graph.nodes(), G)


"""
        # n is the number of pages on the internet
        n = len(I_graph.nodes())
        Q = np.zeros((n,n))


        J = np.ones((n,n))
        G = alpha * Q + (1-alpha) * J/n
"""
