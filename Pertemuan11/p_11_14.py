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
    't':['u','w'],
    'u':['t','v'],
    'v':['u','x'],
    'w':['t','z'],
    'x':['v','w','s'],
    'z':['w'],
    's':['x']
}

g = graph(graph_elements)
g.addEdges({'t','z'})
g.addEdges({'v','s'})
print(g.edges())
