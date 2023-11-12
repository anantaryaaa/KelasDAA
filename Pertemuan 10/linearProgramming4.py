from pulp import LpProblem, LpVariable, LpMaximize

# buat masalah pemrograman linear
lp_problem = LpProblem("Linea_Programming_Example", LpMaximize)

# buat variabel x dan y
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# tambahkan fungsi tujuan (maximize)
lp_problem += 3 * x + 4 * y, "z"

# tambahkan batasan berdasarkan persamaan 4x + 3y = 34 
lp_problem += 3 * x + 4 * y == 11000, "eql"

# selesaikan masalah pemrograman linear 
lp_problem.solve()

# tampilkan hasil
print("Status: ", lp_problem.status)
print("solusi: ")
print(f"x = {x.varValue}")
print(f"x = {y.varValue}")