# Find the index at which two sub arrays are equal in sum
# Eg: input: [4,5,2,3,3,1] 
# output: [4,5] [2,3,3,1] at index 1
# Running time: O(n), optimized approach

def EqualSumSubarray(arr):
    # Optimized approach
    total_sum = 0
    sum_mid = 0
    for i in range(0, len(arr)):
        total_sum = total_sum + arr[i]
    mid_value = total_sum/2
    for j in range(0, len(arr)):
        sum_mid = sum_mid + arr[j]
        if sum_mid == mid_value:
            return j
    return -1
    
    
my_arr = [4,5,2,3,3,1] 
return_index = EqualSumSubarray(my_arr)
if return_index == -1:
    print("No equal sub-groups found")
else:
    print("Equal group at index", return_index)
    print(my_arr[0:return_index+1], my_arr[return_index+1:len(my_arr)+1])
