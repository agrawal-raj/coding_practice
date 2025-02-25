
nums= [7,12,9,11,3,20,35,15]
n = len(nums)

for i in range(n-1):
    for j in range(n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            
print("Bubble Sort: ", nums)

# ============================================================================================================================================4

nums= [7,12,9,11,3,20,35,15]
n= len(nums)

for i in range(n-1):
    min_index= i
    
    for j in range(i+1, n):
        if nums[j] < nums[min_index]:
            min_index= j
    nums[i], nums[min_index] = nums[min_index], nums[i]
print("Selection Sort: ", nums)

    

# ================================================================================================================================================

nums= [7,12,9,11,3,20,35,15]
n= len(nums)

for i in range(1,n):
    insert_index= i
    current_value= nums.pop(i)
    for j in range(i-1, -1,-1):
        if nums[j] > current_value:
            insert_index = j
    nums.insert(insert_index, current_value)

print("Insertion Sort: ", nums)


# ===============================================================================================================================================

def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsorted = [7,12,9,11,3,20,35,15]
sorted = countingSort(unsorted)
print("Counting Sort:", sorted)


# ===============================================================================================================================================


def countingsort(arr):
    max_value= max(arr)
    count= [0] * (max_value+1)
    
    for num in arr:
        count[num] += 1
    
    sorted_arr= []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
        
        

    
    return sorted_arr

arr1= [7,12,9,11,3,20,35,15]
arr2 = countingsort(arr1)
print("Counting Sort: ", arr2)
     
        
# ================================================================================================================

from heapq import merge
def merge_sort(arr):

    if len(arr) <= 1 :
        return arr
    
    mid = len(arr) // 2
    left_half= arr [mid:]
    right_half= arr[:mid]
    
    left_half_sorted= merge_sort(left_half)
    right_half_sorted= merge_sort(right_half)
    
    return merge( left_half_sorted, right_half_sorted)

def merge(left, right):
    result= []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if i < len(left):
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

unsorted= [7,12,9,11,3,20,35,15,-10,-3,2.5]
# sort= merge_sort(unsorted)
# print(sort)
print("Merge Sort :", merge_sort(unsorted))

# =====================================================================================================================================

def mergeSortAuxiliary(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = [0] * mid
    right = [0] * (len(arr) - mid)
    
    for i in range(mid):
        left[i] = arr[i]
    
    for j in range(len(arr) - mid):
        right[j] = arr[mid + j]
    
    sortedLeft = mergeSortAuxiliary(left)
    sortedRight = mergeSortAuxiliary(right)
    
    return merge(sortedLeft, sortedRight)

arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", mergeSortAuxiliary(arr))

# =========================================================
# Quick Sort Program

def partition(array, low , high):
    pivot= array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i +=1 
            array[i] , array[j] = array[j], array[i]
            
    array[i+1] , array[high] = array[high] , array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    
    if low< high:
        pivot_index= partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

arr1= [38, 27, 43, 3, 9, 82, 10] 
quicksort(arr1)
print("Quick Sort: ", arr1) 

# =================================================
#  Quick Sort Program using random pivot element
import random
def partition(arr, low , high):
    pivot= arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1 
            arr[i] , arr[j] = arr[j], arr[i]
            
    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1

def randomized_partition(arr, low, high):
    pivot_index= random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    return partition(arr, low , high)

def random_quicksort(arr, low= 0, high=None):
    if high is None:
        high =  len(arr) -1
        
    if low < high:
        pivot_index=  randomized_partition(arr, low, high)
        random_quicksort(arr, low, pivot_index-1)
        random_quicksort(arr, pivot_index+1, high)

unsort= [38, 27, 43, 3, 9, 82, 10] 
random_quicksort(unsort)
print("Quick Sorted Array: ", unsort)



# ======================================================================================================================================================
array= [7,12,9,11,3,20,35,15]
radix_array= [[],[],[],[],[],[],[],[],[],[]]
max_val= max(array)
exp= 1

while max_val > exp:

    while len(array) > 0:
        val=  array.pop()
        radix_sort=  (val // exp) % 10
        radix_array[radix_sort].append(val)
        
        
    for arr in radix_array:
        while len(arr)> 0:
            val= arr.pop()
            array.append(val)
    
    exp *= 10
    
print("Radix Sort: ", array)
        