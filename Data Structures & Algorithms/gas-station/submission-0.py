class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = [0] * len(cost)

        for i in range(len(gas)):
            total[i] += gas[i] - cost[i]

        sum1 = 0
        index = -1
        for i in range(len(total)):
            sum1 += total[i]
            if sum1 >= 0:
                index = i

        return index