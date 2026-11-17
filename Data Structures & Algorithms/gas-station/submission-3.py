class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        current_gas = 0
        starting_index = 0
        for i in range(len(gas)):
            current_gas += gas[i]
            current_gas -= cost[i]
            if current_gas < 0:
                starting_index = i+1
                current_gas = 0
        return starting_index
        