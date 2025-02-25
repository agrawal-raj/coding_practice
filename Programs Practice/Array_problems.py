# Sorting Without Methods: Bubble Sort

numbers = [5, 2, 9, 1, 7]

# Implement Bubble Sort
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap the elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
