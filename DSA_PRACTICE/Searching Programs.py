def linear_search(arr, target_val):
    for i in range(len(arr)):
        if arr[i] == target_val:
            return i
    return -1

arr= [12,10,45,89,9,35,56]
target_val= 9

result= linear_search(arr, target_val)

if result != -1:
    print("Value", target_val, "found at indexed", result)
    
else:
    print("Value", target_val, "Not Found")


# =================================================================================================
def Binary_search(array, values):
    left= 0
    right= len(array) -1
    while len(array)>0 :
        
        mid=  (left + right) // 2
        
        if array[mid] == values:
            return mid
        
        if array[mid] < values:
            left +=1
        else:
            right +=1
            
    return -1
my_array= [12,10,45,89,9,35,56,15,25]
values =9

res= Binary_search(my_array, values)

if res != -1:
    print("Values", target_val, "found at indexed", res)
else:
    print("Values", target_val,"Not Found")
    

    
    