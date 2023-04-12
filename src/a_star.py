from math import sqrt

class Node:
    def __init__(self, label, weight=0, x=0, y=0):
        self.label = str(label)
        self.weight = weight
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.label == other.label

    def __repr__(self):
        return f'{self.label}'

    def __hash__(self):
        return hash(self.label)


def build(matrix):
    return {Node(i): [Node(j, matrix[i][j], i, j) for j in range(len(matrix[i])) if matrix[i][j] > 0] for i in range(len(matrix))}

def retrace_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

class Graph:
    def __init__(self, matrix, start, goal):
        self.nodes = build(matrix)
        self.start = Node(start)  # Start Node
        self.goal = Node(goal)  # Goal Node

        # Input validation
        if self.start not in self.nodes:
            raise Exception(f'Start node {self.start} not in graph')
        if self.goal not in self.nodes:
            raise Exception(f'Goal node {self.goal} not in graph')

    def euclidean_distance(self, node):
        return sqrt((node.x - self.goal.x) ** 2 + (node.y - self.goal.y) ** 2)

    def calculate(self):
        open_set = {self.start}
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.euclidean_distance(self.start)}

        while len(open_set) > 0:
            current = min(open_set, key=lambda x: f_score[x])
            if current == self.goal:
                return retrace_path(came_from, current), g_score[self.goal]
            open_set.remove(current)
            for neighbor in self.nodes[current]:
                tentative_g_score = g_score[current] + neighbor.weight
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.euclidean_distance(neighbor)
                    if neighbor not in open_set:
                        open_set.add(neighbor)
        return None

if __name__ == '__main__':
    with open('test.txt') as f:
        adj_matrix = [[int(x) for x in line.split()] for line in f.readlines()]
    graph = Graph(adj_matrix, 0, 7)

    print(graph.calculate())