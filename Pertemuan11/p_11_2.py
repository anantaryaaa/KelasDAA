# latihan
# t---u---v
# |       |
# w-------x
# |       |
# z       s

graph = {
    't':['u','w'],
    'u':['t','v'],
    'v':['u','x'],
    'w':['t','z'],
    'x':['v','w','s'],
    'z':['w'],
    's':['x']
}

print(graph)