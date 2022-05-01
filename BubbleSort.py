def bubbleSortAlgorithm(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp

    return arr
arr = [2,5,6,1,4,8,9,6,1]
print(bubbleSortAlgorithm(arr))