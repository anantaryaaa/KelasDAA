import numpy as np 
from scipy.optimize import linprog 

# set the inequality constraints matrix
# note : the inequality constraints must be in the form of <= 
a = np.array([[1,1], [2,3], [1,1], [-1,0], [0,-1]])

# set the inequality constraints vector
b = np.array([16, 19, 8, 0, 0])

# set the coefficients of the linear objective function vector 
note : when maximizing, change the signs 

# belum beres

