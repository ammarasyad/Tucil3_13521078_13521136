import math
from typing import List

def convert(adj: dict):
    return {k: {(v, w) for v, w in adj[k]} for k in adj}


def get_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __getitem__(self, item):
        return (self.x, self.y)[item]

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'


def get_neighbors(matrix, i, j):
    neighbors = set()
    if i > 0 and matrix[i - 1][j] == 1:
        neighbors.add(Node(i - 1, j))
    if i < len(matrix) - 1 and matrix[i + 1][j] == 1:
        neighbors.add(Node(i + 1, j))
    if j > 0 and matrix[i][j - 1] == 1:
        neighbors.add(Node(i, j - 1))
    if j < len(matrix[i]) - 1 and matrix[i][j + 1] == 1:
        neighbors.add(Node(i, j + 1))
    return neighbors if len(neighbors) > 0 else None


class Map:
    def __init__(self, adj_matrix: List[List[int]]):
        self.adj_matrix = self.build_map(adj_matrix)

    def build_map(self, matrix):
        return {Node(i, j): get_neighbors(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))}

    def __getitem__(self, item):
        return self.adj_matrix[item]

    def __contains__(self, item):
        return item in self.adj_matrix.keys()


class Graph:
    def __init__(self, adj_list, start, end):
        if not isinstance(adj_list, Map):
            adj_list = Map(adj_list)
        # if not isinstance(adj_list, dict):
        #     adj_list = convert(adj_list)
        self.adj_list = adj_list
        if not isinstance(start, Node):
            start = Node(*start)
        if not isinstance(end, Node):
            end = Node(*end)

        self.start = start
        self.end = end

        # Input validation
        if self.start not in self.adj_list:
            raise ValueError(f'{self.start} is not in the graph')
        if self.end not in self.adj_list:
            raise ValueError(f'{self.end} is not in the graph')

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def get_neighbors(self, v):
        return self.adj_list[v]

    def get_heuristic(self, v):
        return math.sqrt((self.end[0] - v[0]) ** 2 + (self.end[1] - v[1]) ** 2)

    def calculate(self):
        open_set = {self.start}  # set of nodes to be evaluated
        closed_set = set()  # set of nodes already evaluated
        optimal_path = {self.start: 0}  # distance from start along optimal path
        nav_map = {self.start: self.start}  # map of navigated nodes

        while len(open_set) > 0:
            current = None
            for v in open_set:
                if current is None or nav_map[v] + self.get_heuristic(v) < nav_map[current] + self.get_heuristic(current):
                    current = v

            if current is None:
                break

            if current == self.end:
                path = []

                while nav_map[current] != current:
                    path.append(current)
                    current = nav_map[current]

                path.append(current)
                return path[::-1]

            # for node, weight in self.get_neighbors(current):
            #     if node not in open_set and node not in closed_set:
            #         open_set.add(node)
            #         nav_map[node] = current
            #         optimal_path[node] = optimal_path[current] + weight
            #     else:
            #         if optimal_path[current] + weight < optimal_path[node]:
            #             optimal_path[node] = optimal_path[current] + weight
            #             nav_map[node] = current
            #
            #             if node in closed_set:
            #                 closed_set.remove(node)
            #                 open_set.add(node)

            open_set.remove(current)
            closed_set.add(current)

        return None


if __name__ == '__main__':
    adj_matrix = [[0, 1, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0],
                  [0, 0, 1, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0]]
    # matr = {
    #     (0, 0): {((1, 0), 1), ((0, 1), 1)},
    #     (0, 1): {((1, 1), 1), ((0, 0), 1)},
    #     (1, 0): {((0, 0), 1), ((1, 1), 1)},
    #     (1, 1): {((0, 1), 1), ((1, 0), 1)},
    # }
    graph = Graph(adj_matrix, (0, 0), (7, 7))

    print(graph.calculate())