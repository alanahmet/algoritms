import collections
import copy
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    l, r = mergeSort(arr[:len(arr) // 2]), mergeSort(arr[len(arr) // 2:])
    res, i, j = [], 0, 0
    while i < len(l) or j < len(r):
        if i < len(l) and 
    return res

print(mergeSort([5, 4, 3, 2, 1]))