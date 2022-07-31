class Solution:
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]


"""My dummie
        l, r = 0, len(arr) - 1
        ci = (l + r) // 2
        while r >= l:
            m = (l + r) // 2
            if arr[m] - x == 0 or l == r :
                ci = m
                break
            if arr[m] - x < 0:
                l = m + 1
            else:r = m

        return arr[l:l + k]
"""