rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i) + "*" * i)

for i in range(rows, 0, -1):
    print(" " * (rows-i) + "*" * i)
# =========================================  
"""
OUTPUT: 
    *
   **
  ***
 ****
*****
*****
 ****
  ***
   **
    * 
    """
# =========================================

rows1= 5
for i in range(1, rows+1):
    print("*" * i)
for i in range(rows, 0,-1):
    print("*" * i)

"""
OUTPUT:
*
**
***
****
*****
*****
****
***
**
*
""" 
# ================================
rows= 5
for i in range(1, rows+1):
    print(" " * (rows - i) + "*" * (2*i-1))
for i in range(rows, 0, -1):
    print(" " * (rows-i) + "*" * (2*i-1))
	
"""
OUTPUT:
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""    
#  ==============================================================   
rows1=5
for j in range(rows1,0,-1):
    print(" " * (rows - j) + "*" * (2*j-1))
for j in range(1, rows1+1):
    print(" " * (rows - j) + "*" * (2*j-1))
	
"""
OUTPUT: 

*********
 *******
  *****
   ***
    *
    *
   ***
  *****
 *******
*********
"""	
# ===================================================================
# Hollow Pyramid
rows =5 
for i in range(1, rows+1):
    if  i == 1 or i == rows:
        print(" " * (rows-i) + "*" * (2 * i - 1))
    else:
        print(" " * (rows - i) + "*" + " " * (2*i-3) + '*')

"""
OUTPUT:
    *
   * *
  *   *
 *     *
*********
"""       
# ==================================================================================
# Hollow Diamond
		
rows1=5
for i in range(1,rows1+1):
    if i == 1:
        print(" " * (rows1-i) + "*")
    else:
        print(" " * (rows1-i) + "*" + " " * (2 * i - 3) + "*")
		
for i in range(rows-1, 0,-1):
    if i ==1:
        print(" " * (rows1- i) + "*")
    else:
        print(" " * (rows1 - i) + "*" + " " * (2 * i - 3) + "*")
        
        
"""
OUTPUT:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
# =============================================================================
rows = 5
for i in range(1,  rows+1) :
    print("*" * (2* i-1));

"""
OUTPUT:
*
***
*****
*******
*********
"""
#==============================================================================
rows = 5
for i in range(1,  rows+1) :
    print("*" * (2* i-1));

for i in range(rows-1 ,0 , -1):
    print( "*" * (2 * i-1)); 

"""
OUTPUT:
*
***
*****
*******
*********
*******
*****
***
*
"""
# ================================================================================

rows= 5
for i in range(1, rows+1):
    print(" " * (rows - i) + " ".join(str(j) for j in range(1, i+1)))
    
"""
OUTPUT:
    1
  1 2 3
 1 2 3 4
1 2 3 4 5
"""

# =============================================================================    
n=5
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(' ', end='')
    
    for j in range(1, 2* i):
        if j==1 or j==2 *i-1:
            print(i,end='')
        else:
            print(' ', end='')
    print()

for i in range(4, 0,-1):
    for j in range(1,6-i):
        print(' ', end="")
    
    for j in range(1, 2 * i):
        if j==1 or j==2*i-1:
            print(i, end="")
        else:
            print(' ', end="")
    print()
    
"""
OUTPUT:
    1
   2 2
  3   3
 4     4
5       5
 4     4
  3   3
   2 2
    1
"""

# =================================================================================
n1=5
for i in range(n1, 0 ,-1):
    print(" " * (n1-i) + " ".join(str(j) for j in range(1, i+1)))


"""
OUTPUT:
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""