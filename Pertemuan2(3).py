import numpy as np

def add(a, b):
    result = []
    for first, second in zip(a, b):
        result.append(first + second)
    return result

a = [1, 2, 3]
b = [4, 5, 6]

hasil = add(a, b)
print("hasil:", hasil)