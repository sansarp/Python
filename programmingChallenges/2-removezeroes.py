# Move each zero to end of array without changing the order
# each current element Eg: input: [3, 7, 0, 4, 3, 0, 5, 0] 
# output: [3,7,4,3,5,0,0,0]
# Takes O(n) time


def moveZeroToEnd(arr):
    non_zero = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[non_zero] = arr[i]
            non_zero += 1
    for j in range(non_zero, len(arr)):
        arr[j] = 0
    return arr
    
    
my_arr = [3, 0,8,7, 0, 0,0,0, 4, 3, 0, 5, 0] 
print moveZeroToEnd(my_arr)
