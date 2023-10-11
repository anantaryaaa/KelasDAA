# Judul: **Menentukan Nilai Maksimal dalam Sebuah Deret Bilangan**
#
# Komentar:
# ```python
def nilaiMaksimal(deretBilangan):
    # Fungsi ini digunakan untuk menentukan nilai maksimal dalam suatu deret bilangan.
    nilaiTerbesar = deretBilangan[0]

    # Loop untuk memeriksa setiap nilai dalam deret bilangan
    for nilai in deretBilangan:
        if nilai > nilaiTerbesar:
            nilaiTerbesar = nilai

    return nilaiTerbesar

a = [20, 100, 400, 500, 2]
print(a)  # Mencetak deret bilangan 'a'
print("Nilai terbesar adalah: ", nilaiMaksimal(a))
# Memanggil fungsi 'nilaiMaksimal' untuk mencari nilai maksimal dalam deret 'a' dan mencetak hasilnya.
#
# Kode di atas adalah implementasi dari fungsi `nilaiMaksimal` yang digunakan untuk menentukan nilai maksimal dalam suatu deret bilangan. Fungsi ini mengambil deret bilangan sebagai parameter dan menggunakan loop untuk membandingkan setiap nilai dalam deret dengan nilai terbesar saat ini. Jika nilai dalam deret lebih besar dari nilai terbesar saat ini, maka nilai terbesar diperbarui.
#
# Kemudian, deret bilangan `a` didefinisikan, dicetak ke layar, dan fungsi `nilaiMaksimal` dipanggil untuk mencari nilai maksimal dalam deret `a`. Hasilnya dicetak bersama dengan pesan yang sesuai.