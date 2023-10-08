from re import A
import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools

#try all tours (exact_TSP)
def exact_TSP(cities):
  "generate all posible tours of the cities and choose the shortest one."
  return shortest(alltours(cities))

def shortest(tours):
  "return the tout eith the minimum total distance"
  return min(tours, key=total_distance)

#representing tours
alltours=itertools.permutations # the permutation function is already defined i the itertools module

cities = {1, 2, 3}

list(alltours(cities))

alltours({1,2,3,4})

#representing cities and distance
def total_distance(tour):

  "the total distance between each pair of consecutive cities in the tour"
  return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))

City = complex #constructor for new cities , e.g. City(300, 400)

def distance (A, B):
  "the distance between two points."
  return abs(A-B)


A=City(300, 0)
B=City(0, 400)
distance(A, B)

def Cities(n):
  "make a set of n cities, each with random coordinates"
  return set(City(random.randrange(10, 890), random.randrange(10, 590))for c in range(n))

#lets make some standard sets of cities of various sizes.
#we'll set the random seed so that these sets are the same every time we run this notebook.
random.seed('seed')
cities8, cities10, cities100, cities1000 = Cities(8), Cities(10), Cities(100), Cities(1000)
cities8

tour = exact_TSP(cities8)

print(tour)
print(total_distance(tour))


# try all non-redunant tours
def alltours(cities):
  "return a list of tours, each a permutation of cities, but  each one starting with the same city"
  start = first(cities)
  return [[start] + list(tour)
          for tour in itertools.permutations(cities - {start})]


def first(collection):
  "start iteraating over collection, and return the first element"
  for x in collection:
    return x


alltours({1, 2, 3})
alltours({1, 2, 3, 4})
tour = exact_TSP(cities8)

print(tour)
print(total_distance(tour))

#greedy algorithm

def greedy_algorithm(cities, start=None):
  C = start or first(cities)
  tour = [C]
  unvisited = set(cities - {C})
  while unvisited:
    C = nearest_neighbor(C_unvisited)
    tour.append(C)
    unvisited.remove(C)
    return tour
    def first(collection): return next(iter(collection))
    def nearest_neighbor(A,cities):
      return min(cities, key=lambda C: distence_points(C,A))

  def plot_tour(algorithm, cities):
    "Apply a TSP algorithm to cities, and plot the resulting tour."

    t0 = time.time()
    tour = algorithm(cities)
    t1 = time.time()

    plotline(list(tour) + [tour[0]])
    plotline([tour[0]], 'rs')
    plt.show()
    print("{} city tour; total distance = {:.1f}; time = {:.3f} secs for {}".format(
      len(tour), total_distance(tour), t1 - t0, algorithm.__name__))

def plotline(points, style='bo-'):
  "Plot a list of points (complex numbers) in the 2-D plane."
  X, Y = XY(points)
  plt.plot(X, Y, style)

def XY(points):
  "Given a list of points, return two lists: X coordinates, and Y coordinates."
  return [p.real for p in points], [p.imag for p in points]

plot_tour(exact_TSP, cities8)

plot_tour(exact_TSP, cities10)
def greedy_TSP(cities):
  "At each step, visit the nearest neighbor that is still unvisited."
  start = first(cities)
  tour = [start]
#greedy nearest neighbor (greedy_tsp)
def greedy_TSP(cities):
  "At each step, visit the nearest neighbor that is still unvisited."
  start = first(cities)
  tour = [start]
  unvisited = cities - {start}
  while unvisited:
    C = nearest_neighbor(tour[-1], unvisited)
    tour.append(C)
    unvisited.remove(C)
  return tour

def nearest_neighbor(A, cities):
  "Find the city in cities that in nearest to city A."
  return min(cities, key=lambda x: distance(x, A))
  unvisited = cities - cities = Cities(9)
plot_tour(exact_TSP, cities)
plot_tour(greedy_TSP, cities)
     {start}
  while unvisited:
    C = nearest_neighbor(tour[-1], unvisited )
    tour.append
    unvisited.remove(C)
    return tour

def nearest_neighbor(A, cities):
  "Find the cities that iss nearest to city A."
  return min(cities, key=lambda x: distance(x, A))

plot_tour(greedy_TSP, cities100)
plot_tour(greedy_TSP, cities1000)

#Compare greedy_TSP to all_greedy_TSP
plot_tour(greedy_TSP, cities100)
plot_tour(all_greedy_TSP, cities100)

#algorithm 3: Greeedy Nearest neighbor from all starting points (all_greedy_TSP)
def all_greedy_TSP(cities):
  "Try the greedy algorithm from each of the starting cities; returnthe sortes tour."
  return shortest(greedy_TSP(cities, start=c) for c in cities)

#we will modify greedy_TSP to take an optional start city; otherwise it is unchanged.

def greedy_TSP(cities, start=None):
  "At each step, visit the nearest neighbor that is stil unvisited"
  if start is None: start = first(cities)
  tour = [start]
  unvisited = cities - {start}
  while unvisited:
    C = nearest_neighbor(tour[-1], unvisited)
    tour.append(C)
    unvisited.remove(C)
  return tour

#Compare greedy_TSP to all_greedy_TSP
plot_tour(greedy_TSP, cities100)
plot_tour(all_greedy_TSP, cities100)
#algorithm 4: Greedy Nearest neighbor with exact End (greedy_exact_end_TSP)
def greedy_exact_end_TSP(cities, start=None, end_size=8):
  """At each step, visit the nearest neighbor that is still unvisited untill
  there are k_end cities left; then choose the best of all possible endings"""
  if start is None: start = first(cities)
  tour = [start]
  unvisited = cities - {start}
  #unvisited greedy algortihm fo all but the last end_size cities
  while len(unvisited) > end_size:
    C = nearest_neighbor(tour[-1], unvisited)
    tour.append(C)
    unvisited.remove(C)
  #Consider all permutation of possible ends to the tour, and choose the best one.
  #(but to make things faster, omit the middle of the tour.)
  ends = map(list, itertools.permutations(unvisited))
  best = shortest([tour[0], tour[-1]] + end for end in ends)
  return tour + best[2:]

plot_tour(greedy_exact_end_TSP, cities100)
plot_tour(greedy_exact_end_TSP, cities1000)

#algorithm 5: greedy nearest neighbor with both end search (greedy_bi_TSP)
def greedy_bi_TSP(cities, start_size=12, end_size=6):
  "At each step, visit the nearest neighbor that is still unvisited"
  starts = random.sample(cities, min(len(cities), start_size))
  return shortest(greedy_exact_end_TSP(cities, start, end_size)
   for start in starts)

random.seed('bi')
plot_tour(greedy_bi_TSP, cities100)
plot_tour(greedy_bi_TSP, cities1000)

# benchmarking algorihtm
def compare_algorithms(algorithms, maps):
  "Apply each algorithm to each map and plot result."
  for algorithm in algorithms:
    t0 = time.time()
    results = [total_distance(algorithm(m)) for m in maps]
    t1 = time.time()
    avg = sum(results) / len(results)
    label = '{:.0f}; {:.1f}s: {}'.format(avg, t1 - t0, algorithm.__name__)
    plt.plot(sorted(results), label=label)
  plt.legend(loc=2)
  plt.show()
  print('{} x {}-city maps'.format(len(maps), len(maps[0])))

def Maps(M, N):
  "Return a list of M maps, each consisting of a set N cities"
  return [Cities(N) for m in range(M)]

compare_algorithms([greedy_TSP, greedy_exact_end_TSP],  Maps(100, 50))

def bi_10_6(cities): return greedy_bi_TSP(cities, 10, 6)
def bi_20_5(cities): return greedy_bi_TSP(cities, 20, 5)
def bi_40_4(cities): return greedy_bi_TSP(cities, 40, 4)
def bi_80_2(cities): return greedy_bi_TSP(cities, 80, 2)
def bi_160_1(cities): return greedy_bi_TSP(cities, 160, 1)

algorithms = [bi_10_6, bi_20_5, bi_40_4, bi_80_2, bi_160_1]

compare_algorithms(algorithms, Maps(100, 5))
compare_algorithms(algorithms, Maps(50, 100))

compare_algorithms(algorithms, Maps(25, 160))
