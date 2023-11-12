from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# create Model
model = LpProblem(name="Latihan-Permasalahan", sense=LpMaximize)

# initialize tha variables
x = LpVariable(name='x', lowBound=0)
y = LpVariable(name='y', lowBound=0)

# add the constraint to the model
model += (x + 7 * y == 15000)
model += (3 * x + 4 * y == 11000)

# objective function
# obj_func = 2 * x + 6 * y 
model += lpSum([2 * x + 6 * y])

# solve the problem 
status = model.solve()

print(f"status : {model.status}, {LpStatus[model.status]}")
print(f"objective : {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
    print(f"{var.name}: {var.value()}")




