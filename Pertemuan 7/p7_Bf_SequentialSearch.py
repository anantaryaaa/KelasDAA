# pencarian sequential dalam sebuah list

def sequentialSearch(alist, item):
    # Fungsi ini mengimplementasikan pencarian sekuensial dalam sebuah list.
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

tesList = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# List tesList adalah list yang akan dicari.

# Memanggil fungsi sequentialSearch untuk mencari apakah 3 ada dalam tesList.
print(sequentialSearch(tesList, 3))  # Akan mencetak False karena 3 tidak ditemukan.

# Memanggil fungsi sequentialSearch untuk mencari apakah 2 ada dalam tesList.
print(sequentialSearch(tesList, 2))  # Akan mencetak True karena 2 ditemukan.