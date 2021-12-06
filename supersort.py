def merge (M,N):
    merged_list = []

    m, n = len(M), len(N)
    i, j = 0, 0

    while (i + j < m + n):
        if i == m:
            merged_list.append(N[j])
            j += 1
        elif j == n:
            merged_list.append(M[i])
            i += 1
        elif M[i] <= N[j]:
            merged_list.append(M[i])
            i += 1
        elif M[i] > N[j]:
            merged_list.append(N[j])
            j += 1

    return merged_list

def supersort(L, left, right):
    if len(L) < 1:
        return []
    
    forward_sorted = []
    backward_sorted = []

    # Forward Selection
    current_highest = L.pop(left)
    forward_sorted.append(current_highest)
    right -= 1

    pointer = left
    while (pointer < right):
        if L[pointer] >= current_highest:
            current_highest = L.pop(pointer)
            forward_sorted.append(current_highest)
            right -= 1
        pointer += 1
    
    # Backward Selection
    if right > 1:
        current_highest = L.pop(right-1)
        backward_sorted.append(current_highest)
        right -= 1
        pointer = right-1
        while (pointer >= left):
            if L[pointer] >= current_highest:
                current_highest = L.pop(pointer)
                backward_sorted.append(current_highest)
                right -= 1
            pointer -= 1
            
    
    parent_sorted = merge(forward_sorted, backward_sorted)

    middle = right // 2

    left_list = supersort(L[left:middle], 0, middle)
    right_list = supersort(L[middle:right], 0, right - middle)

    child_sorted = merge(left_list, right_list)

    return merge(parent_sorted, child_sorted)




# # Random Input
from random import randint
L = [randint(0,1000) for i in range(1000000)] # random dari 0 sampai 100000  dengan jumlah data 100



import time
start_time = time.time()

print(f"Unsorted list {L}")
result = supersort(L, 0, len(L))
print(f"Sorted list   {result}")

print("--- %s seconds ---" % (time.time() - start_time))