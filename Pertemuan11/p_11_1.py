# a------b
# |      | 
# |      |
# c------d-----e 

# create the dictionary with graph elements
graph = {
    "a":["b", "c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["b","c","e"],
    "e":["d"]
}

# print the graph
print(graph)