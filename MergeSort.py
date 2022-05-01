def mergeSort(arr):

    if len(arr) > 1:
        mid = int(len(arr)/2)
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    return arr

liste = [1,2,5,8,9,6,2,1,5,6,2,5,9,6,5]
print(mergeSort(liste))

