#Daily Practice
import math
num = int(input("enter a number:"))
x= math.factorial(num)
print(x)
===========================================================================

num = int(input("enter a number:"))
temp= num
rev=0
while num > 0:
    rem= num % 10
    rev = rev *10 + rem
    num = num // 10 
    
if temp == rev :
     print(f"{temp} is palaindrom")
else:
    print(f"{temp} is not palaindrom")
    
    
===============================================================================================
n= int(input("enter a number: "))
if n<=1:
    print("not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
        


======================================================================================================
	num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
    
    
    
 =====================================================================================================
 n = int(input("Enter the number of terms: "))

t1, t2 = 0, 1

print("Fibonacci Series:", t1, t2, end=" ")
for _ in range(2, n):  # Start from the 3rd term
    t3 = t1 + t2
    print(t3, end=" ")
    t1, t2 = t2, t3
    
    
    
 ======================================================================================================
 
 num =  int(input("enter a number: "))
 sum = 0

 while num > 0:
     sum = sum + num % 10
    num //= 10
    
 print(f"{sum} total number of sum ")

========================================================================================================

num1= int(input("Enter First Number")
num2= int(input("Enter Second Number")

print("Before Swaping: ",num1,num2)
num1,num2 = num2, num1
print("After Swaping: ", num1,num2)


=================================================================================================
name= input("enter a name")
sub1= int(input("science marks:"))
sub2= int(input("maths marks:"))
total= sub1 + sub2
print("total marks" , total)


dist1= int(input("distance 1:"))
dist2= int(input("distance 2:"))
sub= dist1 - dist2
print("dist between ", sub)

==============================================================================================================================
num= 12345

b= list(str(num))
b.reverse()
result = int("".join(map(str, b)))
print(result)

==============================================================================================================================
num = int(input("Enter a Number: "))

if (num % 2) == 0:
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")



===================================================================================================================
num= int(input("Enter a Number:"))
temp=num
a=0
if num >=1 and num <= 9:
    print(f"{num} is a Amstrong ")
else:
    for i in range(2,num+1):
        rem= num % 10
        a = rem * rem * rem + a
        num = num // 10
        
    if temp==a:
        print(f"{temp} is a Amstrong")
    else:
        print(f"{temp} is not a Amstrong")