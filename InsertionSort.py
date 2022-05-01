def insertionSort(arr):
    for i in range(len(arr)):

        current = arr[i]
        position = i

        while position > 0 and arr[position-1] > current:
            arr[position] = arr[position-1]
            position = position - 1

        arr[position] = current
    return arr

liste =[1,8,2,4,48,28,79,11]
print(insertionSort(liste))