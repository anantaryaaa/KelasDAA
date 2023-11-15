# menampilkan sudut pada graph

class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def edges (self):
        return self.findedges()
    
# find the distinct list of edges
    def findedges (self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict [vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
# create the dictionary with graph elements
graph_elements = {
     "a":["b", "c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["b","c","e"],
    "e":["d"]
}

g = graph(graph_elements)
print(g.edges())

