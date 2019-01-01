# Get a new array by multiplying prev and next element for
# each current element Eg: input: [1,5,6,9,10] 
# output: [5,6,45,60,90]

def prev_next_multiplied(arr):
    prev = arr[0]
    arr[0] = prev*arr[1] 
   # print(arr[0])
    for i in range(1, len(arr)-1):
        current = arr[i]
        arr[i] = prev * arr[i+1]
        prev = current
        print(arr[i])    
        
    arr[len(arr)-1] = arr[len(arr)-1] * prev
    return arr
    

my_array = [3, 5, 6,9,10]
ab = prev_next_multiplied(my_array)
print("New array:", ab)
