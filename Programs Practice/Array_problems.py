# Sorting Without Methods: Bubble Sort

numbers = [5, 2, 9, 1, 7]

# Implement Bubble Sort
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap the elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# Write a program to find BIGGEST AND SMALLEST ELEMENT in the given array?
arr = [45,62,78,23,89,98]

# Find the biggest element  

max_element = arr[0]
for i in range(len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print("The biggest element is:", max_element)

# Find the smallest element

min_element = arr[0]
for i in range(len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]

print("The smallest element is:", min_element)


# Write a program to find the second smallest element in the given array?   

arr = [45,62,78,23,89,98]

# Find the second smallest element

min_element = arr[0]
second_min_element= arr[0]
for i in range(len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
        second_min_element = min_element
        continue
    if arr[i] > min_element and arr[i] < second_min_element:
        second_min_element = arr[i]

print("The second smallest element is:", second_min_element)



# Write a program to find the second largest element in the given array?    

arr = [45,62,78,23,89,98]

# Find the second largest element

max_element = arr[0]
second_max_element = arr[0]

for i in range(len(arr)):
    if arr[i] > max_element:
        second_max_element = max_element
        max_element = arr[i]
        continue
    if arr[i] < max_element and arr[i] > second_max_element:
        second_max_element = arr[i]

print("The second largest element is:", second_max_element)

# ====================================================================================
# Write a program to DISPLAY MISSING ELEMENT in a given sorted array?

arr = [1,2,3,4,6,7,9,10]   

full_range= set(range(1,11))

arr_set= set(arr)

missing_num = sorted(full_range - arr_set)
if missing_num:
    
    print(missing_num)
else:
    print("No missing element found")

# =================================================================================================
# Write a program to find the PALINDROME numbers in the given ARRAY?

arr = [121, 343, 565, 787, 909]

def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindrome_numbers = [num for num in arr if is_palindrome(num)]

print("Palindrome numbers:", palindrome_numbers)

# =================================================================================================