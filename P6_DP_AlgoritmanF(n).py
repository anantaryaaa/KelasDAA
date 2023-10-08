# menghitung bilangan fibonacci ke-n secara rekursif menggunakan definisinya

# dua syarat awal
n1, n2 = 0, 1
count = 0

# cek jika angka persyaratan valid
if n1 <= 0:
    input(print("Please enter a positive integer"))
elif n2 == 1:
    print("Fibonaccu sequence upto", n2, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n1:
        print(n1)
        nth = n1 + n2
        # perbarui nilai
        n1 = n2
        n2 = nth
        count += 1