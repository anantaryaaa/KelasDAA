piring1 = 'manggis'
piring2 = 'pisang'
piring3 = 'kosong'
TempatBuah = [
    {
        'Piring1':piring1,
        'Piring2':piring2,
        'Piring3':piring3
    }
]
print(f'Kondisi awal buah: {TempatBuah}')

def KondisiPertama():
    piring1 = 'kosong'
    piring3 = 'manggis'
    TempatBuah = [
        {
            'Piring1': piring1,
            'Piring2': piring2,
            'Piring3': piring3
        }
    ]
    print(f'Pertukaran setelah kondisi pertama: {TempatBuah}')

def KondisiKedua():
    piring1 = 'Pisang'
    piring2 = 'Kosong'
    TempatBuah = [
        {
            'Piring1': piring1,
            'Piring2': piring2,
            'Piring3': piring3
        }
    ]
    print(f'Pertukaran setelah kondisi kedua: {TempatBuah}')

def KondisiKetiga():
    piring1 = 'Pisang'
    piring2 = 'Manggis'
    piring3 = 'Kosong'
    TempatBuah = [
        {
            'Piring1': piring1,
            'Piring2': piring2,
            'Piring3': piring3
        }
    ]
    print(f"Jadi kondisi akhir buah adalah: {TempatBuah}")

KondisiPertama()
KondisiKedua()
KondisiKetiga()

# pseudocodenya
# Start
#     set piring1 = 'manggis'
#     set piring2 = 'pisang'
#     set piring3 = 'kosong'
#     set tempatbuah = [
#         {
#             'piring1': piring1,
#             'piring2': piring2,
#             'piring3': piring3
#         }
#     ]
#     print "kondisi awal buah:", tempatbuah
#     function kondisipertama()
#         set piring1 = 'kosong'
#         set piring3 = 'manggis'
#         set tempatbuah = [
#             {
#                 'piring1': piring1,
#                 'piring2': piring2,
#                 'piring3': piring3
#             }
#         ]
#         print "pertukaran setelah kondisi pertama:", tempatbuah
#     end function
#     function kondisikedua()
#         set piring1 = 'pisang'
#         set piring2 = 'kosong'
#         set tempatbuah = [
#             {
#                 'piring1': piring1,
#                 'piring2': piring2,
#                 'piring3': piring3
#             }
#         ]
#         print "pertukaran setelah kondisi kedua:", tempatbuah
#     end function
#     function kondisiketiga()
#         set piring1 = 'pisang'
#         set piring2 = 'manggis'
#         set piring3 = 'kosong'
#         set tempatbuah = [
#             {
#                 'piring1': piring1,
#                 'piring2': piring2,
#                 'piring3': piring3
#             }
#         ]
#         print "jadi kondisi akhir buah adalah:", tempatbuah
#     end function
#     call kondisipertama()
#     call kondisikedua()
#     call kondisiketiga()
# End

# Algoritmanya:
# - Deklarasikan variabel beserta nilainya untuk piring1, piring2, dan piring3
# - Buat sebuah variabel bernama tempat buah dengan nilai array berupa list dari variabel piring1, piring2, piring3
# - Kemudian tampilkan variabel tempat buah untuk mengetahui urutan awal buah
# - Buat fungsi bernama kondisi pertama, dalam fungsinya tukar nilai-nilai dari variabel piring1 ke piring3, lakukan hal yang sama untuk piring3
# - Buat variabel tempat buah dengan nilai yang terbaru
# - lalu tampilkan variabel tempat buah untuk mengetahui urutan buah setelah kondisi pertama
# - Buat fungsi bernama kondisi kedua, dalam fungsinya tukar nilai-nilai dari variabel piring1 ke piring2, lakukan hal yang sama untuk piring2
# - Buat variabel tempat buah dengan nilai yang terbaru
# - lalu tampilkan variabel tempat buah untuk mengetahui urutan buah setelah kondisi kedua
# - Buat fungsi bernama kondisi ketiga, dalam fungsinya deklarasikan variabel piring-piring tadi dengan nilai urutan akhir
# - Buat variabel tempat buah dengan nilai yang terbaru
# - Lalu tampilkan variabel tempat buah untuk mengetahui urutan buah setelah kondisi kedua
# - Panggil ketiga fungsi diatas untuk mengeksekusi perintah-perintah yang sudah dibuat
# - Selesai