import numpy as np
"""
lst = [] 
  
n = 10  
print("Please Input 10 Numbers")
for i in range(0, n): 
    ele = int(input("{} Remaining number entries, Please enter another number: ".format(10-len(lst)))) 
    lst.append(ele) # adding the element 
      
lstS = np.sort(lst)
print(lstS) 
"""

n = 10
numList = list(map(int,input("Enter 10 numbers : \n").strip().split()))[:n]
numList = np.sort(numList)
print("Element Value of Array in ascending order\n", numList) 

