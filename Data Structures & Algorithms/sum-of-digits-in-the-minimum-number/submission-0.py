class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in str(nums[0]):
            res += int(i)
        if res % 2 == 1:
            return 0
        else:
            return 1 
