# Uji Keprimaan Angka

# Uji keprimaan

x = int(input('Input satu angka bulat: '))

angkaPrima = True

if x == 0 or x == 1:
    # Angka 0 dan 1 bukan angka prima
    angkaPrima = False
else:
    for i in range(2, (x // 2)):
        if x % i == 0:
            # Jika x dapat dibagi oleh i, maka x bukan angka prima
            angkaPrima = False
            break

if angkaPrima:
    print(x, 'adalah angka prima')
else:
    print(x, 'bukan angka prima')