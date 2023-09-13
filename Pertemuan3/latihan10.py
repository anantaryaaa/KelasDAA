import pandas as pd
mhs = pd.DataFrame([
    ['1', 'Informatika', 50, 30, 20],
    ['2', 'Sistem Informasi', 55, 30, 25],
    ['3', 'Teknik Sipil', 40, 30, 10]
])
mhs.columns = ['No', 'Prodi', 'Mahasiswa', 'Lakilaki', 'Perempuan']
print(mhs)