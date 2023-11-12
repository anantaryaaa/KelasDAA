# latihan soal 2

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# create Model
model = LpProblem(name="Latihan2", sense=LpMaximize)

# initialize tha variables
y = LpVariable(name='y', lowBound=0)    
x = LpVariable(name='x', lowBound=0)

# add the constraint to the model
model += (2 * x + y == 44)

# objective function
# obj_func = 2 * x + 6 * y 
model += lpSum([2 * x + y])

# solve the problem 
status = model.solve()

print(f"status : {model.status}, {LpStatus[model.status]}")
print(f"objective : {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
    print(f"{var.name}: {var.value()}")