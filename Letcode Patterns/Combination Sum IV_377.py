class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        nmap = {0: 1}
        for i in range(1, target + 1):
            nmap[i] = 0
            for n in nums:
                nmap[i] += nmap.get(i - n, 0)

        return nmap[target]
