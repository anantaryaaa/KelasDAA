# penerapan algoritma dynamic dengan fibonacci
# fibonacci dengan while

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

# cek jika angka persyaratan valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonaccu sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # perbarui nilai
        n1 = n2
        n2 = nth
        count += 1