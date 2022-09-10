class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd, summ = 3, sum(arr)
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        while odd <= len(arr):
            for i in range(odd - 1, len(arr)):
                summ += (arr[i] - arr[i - odd] if i - odd != -1 else arr[i])

            odd += 2

        return summ
