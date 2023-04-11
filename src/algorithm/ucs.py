  
class UCS:
    def __init__(self, matrix):
        self.matrix = matrix
        self.queue = []
        
    def getWeight(self, node1, node2):
        return self.matrix[node1-1][node2-1]
    
    def totalWeight(self, route):
        total = 0
        i = 0
        while (i < len(route)-1):
            total += self.getWeight(route[i], route[i+1])
            i += 1
            
        return total
    
    def pushRoute(self, route):
        i = 0
        if (len(self.queue) > 0):
            while (len(self.queue) > i):
                if (self.totalWeight(self.queue[i]) <= self.totalWeight(route)):
                    i += 1
                else:
                    break
                
        
        self.queue.insert(i, route)
        return
    
    def checkNodeInRoute(self, route, node):
        for n in route:
            if n == node:
                return True
                
        return False
    
    def getNextNode(self, routeNow):
        lastNode = routeNow[-1]
        nextNode = []
        edges = self.matrix[lastNode-1]
        
        i = 0
        for i in range(len(edges)):
            if (edges[i] != 0 and not self.checkNodeInRoute(routeNow, i+1)):
                nextNode.append(i+1)
        
        return nextNode
    
    def search(self, source, destination):
        self.queue.append([source])
        solution = []
        while(len(self.queue) > 0):
            routeNow = self.queue.pop(0)
            
            if (routeNow[0] == source and routeNow[-1] == destination):
                solution = routeNow
                break
            
            nextNode = self.getNextNode(routeNow)
            for node in nextNode:
                temp = routeNow.copy()
                temp.append(node)
                self.pushRoute(temp)
            
            
        return solution, self.totalWeight(solution)


if __name__ == '__main__':
    matrix = []
    while (not matrix):
        try:
            filename = input("Masukkan nama file: ")
            with open(filename, 'r') as f:
                for line in f:
                    temp = [int(num) for num in line.split(' ')]
                    matrix.append(temp)
        except:
            print("Masukkan file lain")
            
    ucs = UCS(matrix)

    print(ucs.search(1, 8))