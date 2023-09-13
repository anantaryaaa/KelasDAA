phi = (1 + 5 ** 0.5) / 2
diameter = 5
tinggi = 4

def VolumeKerucut(p,d,t):
    v = round(p*(5/2)*t/3)
    print(v)

VolumeKerucut(phi, diameter, tinggi)

# pseudocodenya
# Start
#     set phi = (1 + 5 ** 0.5) / 2
#     set diameter = 5
#     set tinggi = 4
#     function volumekerucut(p, d, t)
#         set v = round(p * (d / 2) * t / 3)
#         print v
#     end function
#     call volumekerucut(phi, diameter, tinggi)
# End

# Algoritmanya:
# - Deklarasikan variabel phi, diameter, dan tinggi
# - Bikin sebuah fungsi dengan nama VolumeTabung dengan parameter p,d, dan t
# - Masukkan rumus volume tabung ke dalam fungsi, dimana nilai phi, diameter dan tinggi diambil dari parameter fungsi tersebut,
# - Rumus yang sudah dibuat, diberikan atribut round agar mendapat nilai yang digenapkan
# - Kemudian tampilkan hasil rumusnya
# - Panggil fungsi VolumeKerucut, dimana nilai parameternya diambil dari variabel phi, diameter, dan tinggi
# - Selesai