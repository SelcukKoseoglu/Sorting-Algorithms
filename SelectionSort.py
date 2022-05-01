def selectionSort(arr):
    for i in range(len(arr)-1,0,-1):
        positionOfMax = 0

        for location in range(1,i+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = arr[i]
        arr[i] = arr[positionOfMax]
        arr[positionOfMax] = temp
    return arr
liste = [1,4,78,25,22,11,46]
print(selectionSort(liste))
