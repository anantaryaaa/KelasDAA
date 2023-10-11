def faktorial(n):
    # Fungsi rekursif untuk menghitung faktorial dari n
    if n == 1:
        return n
    return faktorial(n - 1) * n

n = int(input("Masukkan nilai n untuk faktorial: "))
# Meminta pengguna untuk memasukkan nilai n

print(f"Hasil dari {n}! adalah", faktorial(n))
# Mencetak hasil faktorial dari n menggunakan rekursi