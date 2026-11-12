from collections import defaultdict
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n 
        prefix[0] = suffix[n-1] = 0 
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i+1]
        for i in range(0, n):
            if prefix[i] == suffix[i]:
                return i
        return -1













                       



        