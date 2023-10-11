# Menghitung Pangkat Bilangan dengan Rekursi

bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))

# Fungsi untuk menghitung bilangan pangkat dengan rekursi
def hitungPangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitungPangkat(bilangan, pangkat - 1)
    return bilangan

# Memanggil fungsi hitungPangkat untuk menghitung hasil pangkat
hasil = hitungPangkat(bilangan, pangkat)

# Mencetak hasil perhitungan
print(f"Hasil: {hasil}")