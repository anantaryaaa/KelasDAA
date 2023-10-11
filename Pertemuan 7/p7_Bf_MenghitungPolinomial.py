# Evaluasi Polinomial dengan Python

def polinomialPy(a, x):
    result = 0

    # Untuk setiap n dalam rentang 0 .. len(a)-1
    for n, a_n in enumerate(a):
        # Hitung x^n
        x_Power_n = 1
        for i in range(n):
            x_Power_n *= x
        # Tambahkan a_n * x^n ke hasil akhir
        result += a_n * x_Power_n

    return result

a = [1, 2, 0, 3]  # Koefisien polinomial
x = 1.5
# Nilai x yang akan digunakan dalam evaluasi polinomial.

print(polinomialPy(a, x))