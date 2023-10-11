# Menemukan Jarak Terdekat Antara Titik-titik Acak

from math import sqrt
from random import randint

# Inisialisasi list untuk menyimpan titik-titik
titik = []

# Meminta jumlah titik yang ingin dicari jaraknya dari pengguna
n = int(input('Masukkan jumlah titik yang ingin Anda cari jaraknya: '))

# Menghasilkan titik-titik acak dan menyimpannya dalam list 'titik'
for i in range(0, n):
    titik.append([randint(0, 100), randint(0, 100)])

# Mencetak titik-titik yang dihasilkan
print('Titik:\n', titik)

# Fungsi untuk menghitung jarak antara dua titik
def hitungJarak(lis):
    lisJarak = []
    for i in range(0, len(lis) - 1):
        for j in range(i + 1, len(lis)):
            # Menghitung jarak Euclidean antara dua titik
            jarak = sqrt((lis[i][0] - lis[j][0])**2 + (lis[i][1] - lis[j][1])**2)
            lisJarak.append(jarak)
            print('Titik: ', lis[i], 'Titik: ', lis[j], ': ', jarak)
    return min(lisJarak)

# Mencetak jarak terdekat di antara titik-titik yang dihasilkan
print('Jarak terdekat:\n', hitungJarak(titik))