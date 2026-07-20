# input is k, and a stream of int nums
# whenever an integer is added, we return the kth largest number in the stream
# assuming we should keep the list implemented
# brute force: sort the nums array immediately. move k up that many spots and keep it there
# when we add a number, if its smaller or equal to k, we dont move our index
# if we add a larger number, we move until we find a new distinct number and return that k


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

        
