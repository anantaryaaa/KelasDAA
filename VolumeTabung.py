phi = (1 + 5 ** 0.5) / 2
jari2 = 3
tinggi = 5

def VolumeTabung(p,j,t):
    v = round(p*(j*j)*t)
    print(v)

VolumeTabung(phi, jari2, tinggi)

# pseudocodenya
# Start
#     set phi = (1 + 5 ** 0.5) / 2
#     set jari2 = 3
#     set tinggi = 5
#     function volumetabung(p, j, t)
#         set v = round(p * (j * j) * t)
#         print v
#     end function
#     call volumetabung(phi, jari2, tinggi)
# End

# Algoritmanya:
# - Deklarasikan variabel phi, jari2, dan tinggi
# - Bikin sebuah fungsi dengan nama VolumeTabung dengan parameter p,j, dan t
# - Masukkan rumus volume tabung ke dalam fungsi, dimana nilai phi, jari2 dan t diambil dari parameter fungsi tersebut,
# - Rumus yang sudah dibuat, diberikan atribut round agar mendapat nilai yang digenapkan
# - Kemudian tampilkan hasil rumusnya
# - Panggil fungsi VolumeTabung, dimana nilai parameternya diambil dari variabel phi, jari2, dan tinggi
# - Selesai