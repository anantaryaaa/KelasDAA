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
    't':['u','w'],
    'u':['t','v'],
    'v':['u','x'],
    'w':['t','z'],
    'x':['v','w','s'],
    'z':['w'],
    's':['x']
}

g = graph(graph_elements)
print(g.edges())

