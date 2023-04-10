import math

def convert(adj: dict):
    return {k: {(v, w) for v, w in adj[k]} for k in adj}


def get_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


class Graph:
    def __init__(self, adj_list, start, end):
        if not isinstance(adj_list, dict):
            adj_list = convert(adj_list)
        self.adj_list = adj_list
        self.start = start
        self.end = end

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
                if current is None or optimal_path[v] + self.get_heuristic(v) < optimal_path[current] + self.get_heuristic(current):
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

            for node, weight in self.get_neighbors(current):
                if node not in open_set and node not in closed_set:
                    open_set.add(node)
                    nav_map[node] = current
                    optimal_path[node] = optimal_path[current] + weight
                else:
                    if optimal_path[current] + weight < optimal_path[node]:
                        optimal_path[node] = optimal_path[current] + weight
                        nav_map[node] = current

                        if node in closed_set:
                            closed_set.remove(node)
                            open_set.add(node)

            open_set.remove(current)
            closed_set.add(current)

        return None


if __name__ == '__main__':
    matr = {
        (0, 0): {((1, 0), 1), ((0, 1), 1)},
        (0, 1): {((1, 1), 1), ((0, 0), 1)},
        (1, 0): {((0, 0), 1), ((1, 1), 1)},
        (1, 1): {((0, 1), 1), ((1, 0), 1)},
    }
    graph = Graph(matr, (0, 0), (1, 1))

    print(graph.calculate())