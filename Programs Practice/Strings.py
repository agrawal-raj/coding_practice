# Find Occurrence Number program

from collections import Counter

word = input("")
a= Counter(word)

print(a)

# =================================================================================================================
# Write a program to REVERSE THE WORDS in a SENTENCE
def reverse_words_in_place(input_string):
    words = input_string.split(' ')  # Split the string by spaces
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words with spaces

# # Example usage
input_string = input("Enter a string: ")
result = reverse_words_in_place(input_string)
print("Input String: ", input_string)

print("Reversed String: ", result)
# =================================================================================================================
# write a program to count number of words in string 
string= input("Enter a string: ")
a= string.split()
print("Number of words is:",len(a))

# =================================================================================================================
#  Find duplicate character in string program
s = input("Enter a string : ")
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

# ===================================================================================================
# Write a program to display REVERSE of a STRING

a= "rama and laxmana"[::-1]

print(a)

# ================================================================================================
# Write a program to REVERSE the SENTENCE?


word = "rama and laxmana and sita"

lis =  list(map(str , word.split()))
lis.reverse()

print(' '.join(lis))


# =========================================================================================================
# Write program weather the string is PANGRAM or not?
import string
word = input("Enter a sentence: ")
word = word.lower()

for char in string.ascii_lowercase:
    if char not in word:
        print("Not pangram")
        break
else:
    print("pangram")
    
    
# ==========================================================================================================
#  WAP to display number of Lowercase , Uppercase, Special, Symbols, Spaces and Digits in a string

s = input("Enter a string: ")

special_char= '[@_!#$%^&*()<>?/\|}{~:]'
uppercase= 0
lowercase = 0
special_symbol= 0
spaces = 0
Digits =0

for i in range(len(s)):
    if s[i].isupper():
        uppercase += 1
    elif s[i].islower():
        lowercase +=1
        
    elif s[i].isdigit():
        Digits += 1
    elif s[i].isspace():
        spaces += 1
    elif s[i] in special_char:
        special_symbol += 1

print("No. of uppercase letter",uppercase)
print("No. of lowercase letter",lowercase)
print("No. of special characters", special_symbol)
print("No. of spaces",spaces)
print("No. of decimal number",Digits)


# ==========================================================================================================
# WAP to convert Number into Words
from num2words import num2words

num = 223560  

words = num2words(num)

print(words)

#====================================================================================================
# WAP to display string IntCAP or  Words

string= "pramod reddy pavan chandu"

s= string.title()
print(s)

# ========================================================================================================
# WAP to convert uppercase to lowercase & vice versa

s = "Hello World"

s = s.swapcase()

print(s)

# ====================================================================================================
# write a program to convert integer of string type to integer type without using parse int
s = "123456"

integer = 0

for i in range(len(s)):
    integer = integer * 10 + ord(s[i]) - ord('0')

print(integer)

