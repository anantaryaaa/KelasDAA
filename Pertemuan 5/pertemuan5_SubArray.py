def maxCrossingSum(arr, low, mid, high):
    result = 0
    leftSum = float('-infinity')
    for i in range(mid, low-1, -1):
        result += arr[i]
        if (result > leftSum):
            leftSum = result

    result = 0
    rightSum = float('-infinity')
    for i in range(mid + 1, high + 1):
        result += arr[i]
        if (result > rightSum):
            rightSum = result

    return leftSum + rightSum

def maxSum(arr, low, high):
    if (low == high):
        return arr[low]
    mid = (low + high) // 2
    return max (maxSum(arr, low, mid), maxSum(arr, mid+1, high), maxCrossingSum(arr, low, mid, high))

Array = [-1,-3,-2,-4, 7, 5, 9, 10]
result = maxSum(Array, 0, len(Array)-1)
print(result)