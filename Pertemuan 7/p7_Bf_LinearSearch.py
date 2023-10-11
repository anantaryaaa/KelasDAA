# Mencari Nilai Maksimum dengan Pencarian Linear

# Mencari nilai maksimum dalam pencarian linear

def find_maximum(lst):
    max = None
    for el in lst:
        if max == None or el > max:
            max = el
    return max

test_score = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

# Memanggil fungsi find_maximum untuk mencari nilai maksimum dalam test_score
print(find_maximum(test_score))  # Hasilnya adalah 100
