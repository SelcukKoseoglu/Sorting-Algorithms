import itertools
def threeSum(array):
    n = array[0]
    del array[0]
    l = range(len(array)+1)
    comb = itertools.combinations(l,3)
    for i in comb:
        #print(i)
        s = 0
        for l in i:
            s += l
            #print(s)
        if s == n:
            print("bulundu")
            return True
    return "bulunamadı"
array = [10,1,4,3,2,-1]
threeSum(array)
