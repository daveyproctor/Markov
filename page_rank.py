import networkx as nx
import numpy as np
from graph_viz import graph
from Markov import Markov_process

np.random.seed(10)

def sim(n=4, m=15):
    I_graph = nx.DiGraph()
    nodes = ["FB", "Amazon", "HCP", "LinkedIn"]
    # nodes = range(n)
    edges = np.random.choice(nodes,2*m).reshape(m,2)
    # I_graph.add_edges_from(edges)
    I_graph.add_edge("FB", "HCP")
    I_graph.add_edge("Amazon", "HCP")
    I_graph.add_edge("LinkedIn", "HCP")

    # visualize
    graph(I_graph.edges(), 'di')

    # google transition matrix
    G = nx.google_matrix(I_graph, alpha=1.0)
    # make indexing consistent
    G = np.array(G)
    surfer = Markov_process(I_graph.nodes(), G)
    print(surfer.sample_game(stop=10))
    print(G)
    print(I_graph.node)
    surfer.sim_distribution()

if __name__ == "__main__":
    sim()


"""
from web import web_surfer
    # surfer = web_surfer(I_graph)
"""
