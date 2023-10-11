# penggunaan algoritma brute force untuk melakukan perkalian matriks

# Dua matriks yang akan dikalikan
mat1 = [
    [7, 3],
    [2, 1],
]
mat2 = [
    [5, 4],
    [6, 3],
]

# Matriks hasil perkalian
mat3 = []

# Loop untuk mengalikan matriks
for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

# Loop untuk mencetak matriks hasil
for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print(mat3[x][y], end=' ')
    print()