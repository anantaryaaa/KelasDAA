# ============= BAGIAN BFS ============
# deklarasi fungsi bfs
def bfs (graph, start) :
  visited = []
  queue = []
  queue = [start]
  while queue :
    node = queue.pop(0)
    if node not in visited:
      visited.append(node)
      neigbours = graph[node]
      for neighbour in neigbours:
        queue.append(neighbour)
  return visited

graph = {
  'amin':['wasim', 'nick', 'mike'],
  'wasim':['imran', 'amin'],
  'imran':['wasim', 'faras'],
  'faras':['imran'],
  'mike':['amin'],
  'nick':['amin']
}

print('BFS ALGORITHM')
print('start = amin', bfs(graph,'amin'))
# ===================================================================
def pembatas ():
    print('===================================================================')
# o amin--------------------------
# |                |            |
# o wasim       o nick      o mike
# |
# o imran 
# |
# o faras
print('start = wasim', bfs(graph, 'wasim'))
# ===================================================================
print(pembatas())
print('start = faras', bfs(graph,'faras'))
# ===================================================================
print(pembatas())
# LATIHAN
print('LATIHAN')
# buat bfs dengan skema berikut :
# rektor-------------
# |                 |        
# wakarek 1     wakarek 2
#                   |
# |-----------------|-------------|
# kaprodi 1     kaprodi 2     kaprodi 3
# |                 |             |
# dosen a       dosen d       dosen f
# |                 |             |
# dosen b       dosen e       dosen g
# |
# dosen c
GraphLatihan = {
  'rektor':['wakarek1','wakarek2'],
  'wakarek1':['rektor'],
  'wakarek2':['kaprodi1', 'kaprodi2','kaprodi3','rektor'],
  'kaprodi1':['dosena','dosenb', 'dosenc','wakarek2'],
  'kaprodi2':['dosend','dosene','wakarek2'],
  'kaprodi3':['dosenf','doseng','wakarek2'],
  'dosena':['kaprodi1'],
  'dosenb':['kaprodi1'],
  'dosenc':['kaprodi1'],
  'dosend':['kaprodi2'],
  'dosene':['kaprodi2'],
  'dosenf':['kaprodi3'],
  'doseng':['kaprodi3'],
}
print('LAITHAN BFS ALGORITHM')
print('start = rektor', bfs(GraphLatihan,'rektor'))
# ===================================================================
print(pembatas())
# ============= BAGIAN DFS ============
# deklarasi fungsi dfs
def dfs(visited,graph,node):
  if node not in visited:
    print(node)
    visited.add(node)
    for neighbour in graph:
      dfs(visited,graph,neighbour)

visited = set()
print('DFS ALGORITHM')
print('start = amin', dfs(visited,graph,'amin'))
# ===================================================================
print(pembatas())
visited = set()
print('start = wasim', dfs(visited,graph,'wasim'))
# ===================================================================
print(pembatas())
visited = set()
print('start = faras', dfs(visited,graph,'faras'))
# ===================================================================
print(pembatas())
visited = set()
print('start = nick', dfs(visited,graph,'nick'))
# ===================================================================
print(pembatas())
print('LAITHAN DFS ALGORITHM')
print('start = rektor', dfs(visited,GraphLatihan,'rektor'))

