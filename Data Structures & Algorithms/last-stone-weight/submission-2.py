# understand:
# input: list of stones that is a list of numbers 
# output: an integer, which is weight of remaining stone  or 0 if none remain
# edge cases: stone is empty, only 1 num, negative numbers, 0 

# match: heapq, whole loop

# plan:
# heapify the stones list, but make it a max heap
# we run while len(stones) > 1 
# if heap[0] == heap[1]: then we heappop twice 
# if heap[x] is less than heap[y]
# store both variables and make sure to multiply by -1 as we get them
# pop twice
# add back the value of y-x into the heapq
# once while loop is done, return heap[0] if it exists, else return 0



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)
        while (len(max_heap) > 1):
            top_2 = [ -x for x in heapq.nlargest(2, max_heap) ]
            first = top_2[0]
            second = top_2[1]
            if first == second:
                heapq.heappop_max(max_heap)
                heapq.heappop_max(max_heap)
                continue
            if first < second:
                x_val = first
                y_val = second
                heapq.heappop_max(max_heap)
                heapq.heappop_max(max_heap)
                new_val = y_val - x_val
                heapq.heappush_max(max_heap, new_val)
        if max_heap: return max_heap[0] 
        return 0

            
        