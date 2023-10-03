# mencari bilangan maksimum dan minimum

himpunanBilangan = [4, 12, 23, 9, 21, 1, 35, 2, 24]
bilanganKecil = 100
bilanganBesar = 0

for a in (himpunanBilangan):

    if a < bilanganKecil:
        bilanganKecil = a
    if a > bilanganBesar:
        bilanganBesar = a

print(f"jadi bilangan terkecilnya adalah {bilanganKecil}")
print(f"jadi bilangan terbesarnya adalah {bilanganBesar}")