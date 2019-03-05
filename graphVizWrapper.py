from graphviz import Graph, Digraph

def graph(E, type='', simple=False, name='test'):
    
    if type == 'di':
        G = Digraph()
    else:
        G = Graph()

    edges = set()
    for edge in E:
        edge = tuple(edge)
        if not simple or edge not in edges:
            G.edge(str(edge[0]), str(edge[1]))
            edges.add(edge)

    G.render('visualize/' + name + '.gv', view=False)
    return G
