# menggunakan lib scipy 

from scipy.optimize import linprog

# tentukan koefisien fungsi tujuan dan matriks batasan
# koefisine fungsi tujuan (z = 5 x 1 + 7 x 2)
c = [-5, -7] #karena kita ingin memaksimalkan -5 x 1 - 7 x 2, maka perlu diubah menjadi -5 dan -7 

# koefisien matriks batasan 
a = [
    [1,0], # 1 x 1 + 0 x 2 <= 16
    [2,3], # 2 x 1 + 3 x 2 <= 19
    [1,1] #1 x 1 +  1 x 2 <= 8 
]

# batasan kanan (rhs) dari masing-masing batasan 
b = [16, 19, 8]

# 3. tentukan batasan variabel x1 dan x2 sebagai variabel non-negatif:
x1_bounds = (0,None) #x1 >= 0 
x2_bounds = (0, None) #x2 >= 0 

# 4. gunakan linprog untuk menyelesaikan masalah pemrograman linear:
result = linprog(c, A_ub= a, b_ub = b, bounds = [x1_bounds, x2_bounds], method="highs")

# 5. tampilkan hasilnya 
# hasil optimasi

print("Optimal solution: ")
print("x1 = ", result.x[0])
print("x2 = ", result.x[1])
print("Max z = ", -result.fun) #karena tujuannya adalah memaksimalkan -z

