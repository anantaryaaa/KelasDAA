# inversi dalam suatu array tanpa divide & conquer

def countVersion(arr):
    result = 0
    for i in range(len(arr)):
        # print(i)
        for j in range(i+1, len(arr)):
            # print(j)
            if arr[i] > arr[j]:
                result += 1
    print(result)

arr = [21, 70, 36, 14, 25]
result = countVersion(arr)
print(result)