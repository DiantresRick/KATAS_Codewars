# Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element
# (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge,
#  even if there are more than one with the same value!)
# If array is empty, null or None, or if only 1 Element exists, return 0.
# Note:In C++ instead null an empty vector is used. In C there is no null. ;-)



def sum_array(arr):
    acumulador = 0
    max = -200
    min = 999
    for item in arr or []:
        acumulador = item + acumulador
        if item > max:
            max = item
        if item < min:
            min = item
    if not arr or max == min:
        return 0
    else: return acumulador - (max + min)

    

    if __name__ == "__main__":
        
      
    ## TEST 1   "None or Empty"
        assert(sum_array(None)== 0)

    ## TEST 2   "Only one Element"
        assert(sum_array([3])== 0)
        assert(sum_array([-3])== 0)

    ## TEST 3   "Only two Element"
        assert(sum_array([ 3, 5])== 0)
        assert(sum_array([-3, -5])== 0)

    ## TEST 4   "Real Tests"
        assert(sum_array([6, 2, 1, 8, 10])== 16)
        assert(sum_array([6, 0, 1, 10, 10])== 17)
        assert(sum_array([-6, -20, -1, -10, -12])== -28)
        assert(sum_array([-6, 20, -1, 10, -12])== 3)