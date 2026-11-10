class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        difference = 0
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in hashset:
                return [hashset[difference], i]
            else:
                hashset[nums[i]] = i