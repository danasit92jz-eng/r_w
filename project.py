"""
    *
   **
  ***
 ****
*****
"""
n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")

"""
* * * * * 
*       * 
*       * 
*       * 
* * * * *
"""
n=5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  


"""
*****
****
***
**
*
"""

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

"""
         * 
        * * 
       * * * 
      * * * * 
     * * * * * 
    * * * * * * 
   * * * * * * * 
  * * * * * * * * 
 * * * * * * * * * 
* * * * * * * * * * 
"""
n=10   
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print("")



"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for k in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    for k in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()













