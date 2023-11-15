class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def edges(self):
        return self.findedges()
    
# add new edges
    def addEdges(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# list the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
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
g.addEdges({'r','k'})
g.addEdges({'m','j'})
print(g.edges())
