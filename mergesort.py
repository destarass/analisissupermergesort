#
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
  

    L = [0] * (n1)
    R = [0] * (n2)
  
   
    for i in range(0 , n1):
        L[i] = arr[l + i]
  
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
  
   
    i = 0    
    j = 0    
    k = l     
  
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
  
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
  
   
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
  

def mergeSort(arr,l,r):
    if l < r:
  
       
        m = (l+(r-1))//2
  
       
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
  
  

from random import randint
arr = [randint(0,1000) for i in range(1000000)] # random dari 0 sampai 100000  dengan jumlah data 100
n = len(arr)

import time
start_time = time.time()

print(f"Unsorted list {arr}")
mergeSort(arr,0,n-1)
print(f"Sorted list   {arr}")

print("--- %s seconds ---" % (time.time() - start_time))


