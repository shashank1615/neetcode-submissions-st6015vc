class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has_map = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in has_map:
                return [has_map[diff], i]
            has_map[n] = i
        
            

        