# Find the index at which two sub arrays are equal in sum
# Eg: input: [4,5,2,3,3,1] 
# output: [4,5] [2,3,3,1] at index 1
# Running time: O(n*2)

def EqualSumSubarray(arr):
    # Brute force approach
    sum1 = 0
    for i in range(0, len(arr)):
        sum1 = sum1 + arr[i]
        sum2 = 0
        for j in range(i+1, len(arr)):
            sum2 = sum2 + arr[j]
        if sum1 == sum2:
            return i
    return -1
    
    
my_arr = [4,5,7,3,2,3,3,1,7,3] 
return_index = EqualSumSubarray(my_arr)
if return_index == -1:
    print("No equal sub-groups found")
else:
    print("Equal group at index", return_index)
    print(my_arr[0:return_index+1], my_arr[return_index+1:len(my_arr)+1])
