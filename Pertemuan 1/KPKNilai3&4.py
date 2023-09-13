n = 3
m = 4
resultN = []
resultM = []
result = []

for i in range(1, 10):
    Resultn = n * i
    resultN.append(Resultn)
    Resultm = m * i
    resultM.append(Resultm)

for i in range(0,8):
    Kpkn = resultN[i]
    for i in range(0,8):
        kpkm = resultM[i]
        if Kpkn == kpkm:
            result.append(Kpkn)

print(result[0])

# pseudocodenya
# Start
#     set n = 3
#     set m = 4
#     create empty array resultn
#     create empty array resultm
#     create empty array result
#
#     for i from 1 to 9
#         set resultn = n * i
#         append resultn to resultn
#         set resultm = m * i
#         append resultm to resultm
#     end for
#
#     for i from 0 to 7
#         set kpkn = resultn[i]
#         for j from 0 to 7
#             set kpkm = resultm[j]
#             if kpkn equals kpkm then
#                 append kpkn to result
#             end if
#         end for
#     end for
#
#     print result[0]
# End

# Algoritma
# - Deklarasikan variabel n dan m dengan nilai 3 dan 4
# - Deklarasikan variabel resultN, resultM, dan result dengan list kosong
# - Buat looping dengan jarak 1 sampai 10 yang diwakilkan dengan variabel i
# - Deklarasikan nilai Resultn dengan perhitungan variabel n di kalikan i
# - Tambahkan nilai Resultn ke dalam list resultN
# - Deklarasikan nilai Resultm dengan perhitungan variabel m di kalikan i
# - Tambahkan nilai Resultm ke dalam list resultM
# - Buat looping dengan jarak 0 sampai 8 yang diwakilkan dengan variabel i di luar looping sebelumnya
# - Deklarasikan variabel Kpkn dengan nilai variabel resultN dengan index i
# - Buat looping dengan jarak 0 sampai 8 yang diwakilkan dengan variabel i di dalam  looping sebelumnya
# - Deklarasikan variabel Kpkm dengan nilai variabel resultM dengan index i
# - Buat pengkondisian jika Kpkn sama dengan Kpkm maka variabel Kpkn akan ditambahkan ke variabel result
# - Panggil variabel result index ke 0 di luar looping
# - Selesai