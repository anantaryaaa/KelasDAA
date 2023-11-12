import pulp #import lib pulp

lp_Problem = pulp.LpProblem('Masalah', pulp.LpMinimize) #mendefinisikasn masalah yang ada

x = pulp.LpVariable('x',lowBound=0) #membuat variable x dengan nilai lebih dari 0
y = pulp.LpVariable('y',lowBound=0) #membuat variable y dengan nilai lebih dari 0

y = 6 * x
lp_Problem += 2 * (x + y) #objective function 

# constraints:
lp_Problem += 2 * (x + y) >= 44

# display problem
print(lp_Problem)

status = lp_Problem.solve() #solver
print(pulp.LpStatus[status]) #the solution status 

print(pulp.value(x), pulp.value(y), pulp.value(lp_Problem.objective))





