# Find elements that appear only once
# Eg: input: [4,4,5,5,5,1,3,3,2,8] 
# output: [1,2,8]
# Running time O(n)
# Algorithm: Check each array element -> If already in key 
# then increase its value else add to key with value 0
# Get keys or dict element whose values are 0.

def OnlyOnce(arr):
    elem_dict = {}
    single_valued = []
    for i in range(0, len(arr)):
        if arr[i] in elem_dict:
            elem_dict[arr[i]] += 1
        else:
            elem_dict[arr[i]] = 0
    for key, value in elem_dict.items():
        if value == 0:
            single_valued.append(key)
    return single_valued
    
my_arr = [4,4,5,5,5,1,3,3,2,8] 
vals = OnlyOnce(my_arr)
print("Elements that appear only once are:", vals)




