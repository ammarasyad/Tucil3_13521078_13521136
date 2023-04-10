# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

def parseFile(filename):
    matrix = []
    while (not matrix):
        with open(filename, 'r') as f:
            for line in f:
                temp = [float(num) for num in line.split(' ')]
                matrix.append(temp)
                
    return matrix

def getEdge(matrix) :
    edges = []
    node = len(matrix)
    i = 0
    for i in range(node) :
        for j in range(i, node) :
            if (matrix[i][j] > 0) :
                edges.append((i+1, j+1, matrix[i][j]))
    
    return edges

def createGraphsWithSave(edge_list) :
    G = nx.Graph()
    G.add_weighted_edges_from(edge_list)
    
    pos = nx.planar_layout(G)
    weight = nx.get_edge_attributes(G, 'weight')
    """ nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif") """
    nx.draw_networkx(G, pos, edge_color ='.4')
    nx.draw_networkx_edge_labels(G, pos, weight)
    plt.savefig("temp.png")
    return

def createGraphsWithoutSave(edge_list) :
    G = nx.Graph()
    G.add_weighted_edges_from(edge_list)
    
    pos = nx.planar_layout(G)
    weight = nx.get_edge_attributes(G, 'weight')
    """ nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif") """
    nx.draw_networkx(G, pos, edge_color ='.4')
    nx.draw_networkx_edge_labels(G, pos, weight)
    plt.show()
    return