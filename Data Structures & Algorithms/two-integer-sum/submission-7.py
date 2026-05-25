class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for i, num in enumerate(nums):
            diff = target - num;
            if diff in hash_nums:
                return [hash_nums[diff], i]
            hash_nums[num] = i
        return
        

            

        