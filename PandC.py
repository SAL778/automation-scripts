# -*- coding: utf-8 -*-
"""tp.ipynb

Automatically generated by Colaboratory.

Given a number of objects *n*, plot the number of combinations and permutations those objects would generate in an increasing order. Plot the respective graphs.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def factorial(n):
  return 1 if (n==0 or n==1) else n*factorial(n-1)

n=2
math.pow(2,n)-1     #Combinations, null value excluded
factorial(n)        #Permutations

"""The Y AXIS will be the value of 'n'.
X axis will have two plots - \\
Total number of permutations and Total number of combinations \\
Add a Legend to the graph to help identify P and C.
"""

x1 = np.array(1)   #P
x2 = np.array(1)   #C
y = np.array(1)    #n

#Populating the arrays
while n<=9:
  x1 = np.append(x1,math.pow(2,n)-1)    #Combinations
  x2 = np.append(x2,factorial(n))       #Permutations
  y = np.append(y,n)                    #Number of items tracker
  n+=1

plt.plot(x1,y)      #Combinations
plt.title('Number of Combinations')
plt.ylabel("number of items (n)")
plt.xlabel('Combinations')
plt.show()

plt.plot(x2,y)      #Permutations
plt.title('Number of Permutations')
plt.xlabel('Permutations')
plt.ylabel("number of items (n)")
plt.show()

plt.plot(x2,y)      #Permutations
plt.plot(x1,y)      #Combinations
plt.xlabel("P and C")
plt.ylabel("number of items (n)")
plt.title("Growth of P and C with incease in n")
plt.legend(["no. of Permutations","no. of Combinations"], loc ="lower right")
plt.show()

"""
It might seem like the orange line (number of combinations) hasn't moved but it has!
Try changing the 'n' value in line 16 to see more significant results.
"""