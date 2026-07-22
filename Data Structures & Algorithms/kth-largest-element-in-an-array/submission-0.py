# input: unosryted array nums, integer k
# output: an integer, which is the kth largest element in the array

# edge cases: k = 0, k = 1, nums = 1, k > nums.length(), nums is empty

# min heap of k elements, the top of the min heap will always represent the kth largest element. 
# initialize a min heap
# if len(min_heap) < k, we can push with no problem
# otherweise, if the number we are at is greater than the top of the min heap, we need to psuh out the top number
# we push out the top number, and then add thsi enw number. at the end of the loop, we return the top of our min heap



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]
        