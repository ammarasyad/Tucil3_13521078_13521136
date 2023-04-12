# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

def parseFile(filename):
    with open(filename) as f:
        matrix = [[float(num) for num in line.split(' ')] for line in f]
    for i in matrix:
        if len(i) != len(matrix) or len(i) < 8 or len(matrix) < 8:
            raise Exception('Matrix must be square and at least 8x8')
    return matrix

def getNode(matrix) :
    nodes = []
    node = len(matrix)
    i = 0
    for i in range(node) :
        for w in matrix[i]:
            if w != 0:
                nodes.append(i+1)
                break
        i += 1
    
    return nodes

def getEdge(matrix) :
    edges = []
    node = len(matrix)
    i = 0
    for i in range(node) :
        for j in range(node) :
            if matrix[i][j] > 0:
                edges.append((i+1, j+1, matrix[i][j]))
    
    return edges