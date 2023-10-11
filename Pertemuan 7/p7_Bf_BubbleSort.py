# Pengurutan Bubble (Bubble Sort) dalam Python

def bubbleSort(alist):
    # Fungsi ini mengimplementasikan algoritma pengurutan bubble untuk mengurutkan list 'alist'.
    for passNum in range(len(alist) - 1, 0, -1):
        for i in range(passNum):
            if alist[i] > alist[i + 1]:
                # Jika elemen saat ini lebih besar dari elemen berikutnya, tukar mereka.
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

himpunanBilangan = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# himpunanBilangan adalah list yang akan diurutkan.

bubbleSort(himpunanBilangan)
# Memanggil fungsi bubbleSort untuk mengurutkan himpunanBilangan.

print(himpunanBilangan)
# Mencetak himpunanBilangan yang sudah diurutkan.