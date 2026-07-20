# input is k, and a stream of int nums
# whenever an integer is added, we return the kth largest number in the stream
# assuming we should keep the list implemented
# brute force: sort the nums array immediately. move k up that many spots and keep it there
# when we add a number, if its smaller or equal to k, we dont move our index
# if we add a larger number, we move until we find a new distinct number and return that k


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.sorted_nums.reverse()
        print(self.sorted_nums)
        if k < len(self.sorted_nums):
            kth_num = self.sorted_nums[k-1]
        self.kth = k
        

    def add(self, val: int) -> int:
        self.sorted_nums.append(val)
        self.sorted_nums.sort(reverse=True)
        kth_num = self.sorted_nums[self.kth-1]
        return kth_num

        
