def quickSort(array):
    quickSortRecursion(array,0,len(array)-1)
    return array
def quickSortRecursion(array,first,last):
    if first < last:
        splitpoint = partition(array,first,last)

        quickSortRecursion(array,first,splitpoint-1)
        quickSortRecursion(array,splitpoint+1,last)

def partition(array,first,last):
    pivotvalue = array[0]
    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and array[left] <= pivotvalue:
            left += 1
        while array[right] >= pivotvalue and right >= left:
            right += 1

        if right < left:
            done = True
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

    temp = array[first]
    array[first] = array[left]
    array[left]  = temp
    return right


