# Find Occurrence Number program
'''
from collections import Counter

str = input("")
a= Counter(str)

print(a)
# for i in a.keys():
#     print(i,":", a[i])
# M = set(input())
# N = set(input())

# a= M.symmetric_difference(N)
# b= list(a)
# b.sort()
# print(b)  '''

# =================================================================================================================
# Reverse String Program
'''
def reverse_words_in_place(input_string):
    words = input_string.split(' ')  # Split the string by spaces
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words with spaces

# # Example usage
input_string = input("Enter a Name")
result = reverse_words_in_place(input_string)
print("Input String: ", input_string)

print("Reversed String: ", result)'''
# =================================================================================================================
# write a program to count number of words in string 
str= input("Enter: ")
a= str.split()
print("Number of words is:",len(a))

# =================================================================================================================
#  Find duplicate character in string program
s = input("Enter: ")
freq={}
res=[]
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

for c, a in freq.items():
    if a > 1:
        res.append(c)
print("duplicate values:",res)