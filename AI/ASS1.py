from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSutil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSutil(neighbour, visited)
    def DFS(self, v):
        visited = set()
        self.DFSutil(v, visited)
    
    def BFS(self, s, n):
        visited = [False] * (max(self.graph) + n)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end= " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    s = Graph()   
    n = int(input("Enter the number of Nodes: "))
    for i in range(n):
        node = int(input("Enter the Nodes: "))
        edge = int(input("Enter the Connection: "))
        s.addEdge(node, edge)
    print("The BFS is: ")
    s.BFS(5, n)
    print("\nThe DFS is: ")
    s.DFS(5)