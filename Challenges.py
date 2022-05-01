def second(array):
    for i in range(0,len(array)-1):
        for k in range(i+1):
            if array[k] > array[k+1]:
                temp = array[k]
                array[k] = array[k + 1]
                array[k + 1] = temp


    second_low = array[1]
    second_big = array[len(array)-2]
    print(array)
    print(second_low,second_big)
array = [1,2,7,9,1,2,4]
second(array)