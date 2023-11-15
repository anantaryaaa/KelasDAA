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
    'r':['o','i'],
    'o':['r','m','p'],
    'm':['o','n'],
    'i':['r','p'],
    'p':['o','i','n'],
    'n':['m','p']
}

g = graph(graph_elements)
print(g.edges())

