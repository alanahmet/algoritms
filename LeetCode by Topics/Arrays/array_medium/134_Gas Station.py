class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans, net, summ = 0, 0, 0

        for i in range(len(gas)):
            net += gas[i] - cost[i]
            summ += gas[i] - cost[i]

            if summ < 0:
                summ = 0
                ans = i + 1

        return ans if net >= 0 else -1
