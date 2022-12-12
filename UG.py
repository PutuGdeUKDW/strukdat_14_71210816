class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set()

    def vertex(self): #mencetak seluruh vertex
        print("\nSeluruh Node = ", end = "")
        for key, value in self._data.items():
            print(key, end = ' ')
        print()
    
    def edge(self): #mencetak seluruh edge
        print("Seluruh Edge = ", end = "")
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(f'{str(key)}{str(item)}')
        for item in listEdge:
            print(item, end = ' ')
        print()

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        visited = []
        visited.append(node)
        stack = []
        stack.append(node)
 
        while stack:
            x = stack.pop(0)
            for i in self._data[x]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
                    
        print("Traversing BFS = ",end='')
        for i in visited:
            print(i,end=' ')
        print("\n")

# silahkan buat graph seperti pada soal
graph = Graph()
# misalnya 
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b', 'd')
graph.addEdge('b', 'c')
graph.addEdge('c', 'e')
graph.addEdge('c', 'g')
graph.addEdge('d', 'b')
graph.addEdge('d', 'e')
graph.addEdge('e', 'f')
graph.addEdge('e', 'd')
graph.addEdge('f', 'e')
graph.addEdge('g', 'c')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs("a")
