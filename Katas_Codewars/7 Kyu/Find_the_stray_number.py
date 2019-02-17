# You are given an odd-length array of integers, in which all of them are the same,
# except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3



def stray(arr):
    i = 0
    while i <= len(arr):
        if arr.count(arr[i]) < 2:
            return arr[i]
        else:
            i+=1

if __name__ == "__main__":
    
    assert stray([1, 1, 1, 1, 1, 1, 2])== 2
    assert stray([2, 3, 2, 2, 2])== 3
    assert stray([3, 2, 2, 2, 2])== 3