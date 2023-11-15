# menambahkan simpul vertex

class Graph :
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    # get the keys of the dictionary
    def getVertices (self):
        return list(self.gdict.keys())
    
    # add the vertex as a key
    def addVertex (self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    
# create dictionary with graph elements
graph_elements = {
    "a":["b", "c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["b","c","e"],
    "e":["d"]
}

# create an instance of the Graph class and pass the graph_elements
g = Graph(graph_elements)

g.addVertex('f')

# print the vertices by calling the getVertices method with the parentheses
print(g.getVertices())

