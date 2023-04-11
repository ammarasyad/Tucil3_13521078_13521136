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

def getNode(matrix) :
    nodes = []
    node = len(matrix)
    i = 0
    for i in range(node) :
        for w in matrix[i]:
            if (w != 0):
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
            if (matrix[i][j] > 0) :
                edges.append((i+1, j+1, matrix[i][j]))
    
    return edges