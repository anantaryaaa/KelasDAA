# menampilkan simpul pada graph

class Graph :
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    # get the keys of the dictionary
    def getVertices (self):
        return list(self.gdict.keys())
    
# create dictionary with graph elements
graph_elements = {
    'r':['o','i'],
    'o':['r','m','p'],
    'm':['o','n'],
    'i':['r','p'],
    'p':['o','i','n'],
    'n':['m','p']
}

# create an instance of the Graph class and pass the graph_elements
g = Graph(graph_elements)

# print the vertices by calling the getVertices method with the parentheses
print(g.getVertices())

