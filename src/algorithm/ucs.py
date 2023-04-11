def check_node_in_route(route, node):
    return node in route


class UCS:
    def __init__(self, matrix):
        self.matrix = matrix
        self.queue = []
        
    def get_weight(self, node1, node2):
        return self.matrix[node1-1][node2-1]
    
    def total_weight(self, route):
        return sum([self.get_weight(route[i], route[i + 1]) for i in range(len(route)-1)])

    def push_route(self, route):
        i = 0
        if len(self.queue) > 0:
            while len(self.queue) > i:
                if self.total_weight(self.queue[i]) > self.total_weight(route):
                    break
                i += 1

        self.queue.insert(i, route)
        return

    def get_next_node(self, current_route):
        last_node = current_route[-1]
        next_node = []
        edges = self.matrix[last_node-1]
        
        for i in range(len(edges)):
            if edges[i] != 0 and not check_node_in_route(current_route, i + 1):
                next_node.append(i+1)
        
        return next_node
    
    def search(self, source, destination):
        self.queue.append([source])
        solution = []
        while len(self.queue) > 0:
            route_now = self.queue.pop(0)
            
            if route_now[0] == source and route_now[-1] == destination:
                solution = route_now
                break
            
            next_node = self.get_next_node(route_now)
            for node in next_node:
                temp = route_now.copy()
                temp.append(node)
                self.push_route(temp)
            
            
        return solution, self.total_weight(solution)


if __name__ == '__main__':
    matrix = []
    while not matrix:
        try:
            filename = input("Masukkan nama file: ")
            with open(filename, 'r') as f:
                for line in f:
                    temp = [int(num) for num in line.split(' ')]
                    matrix.append(temp)
        except IOError | ValueError | FileNotFoundError:
            print("Masukkan file lain")
            
    ucs = UCS(matrix)

    print(ucs.search(1, 8))