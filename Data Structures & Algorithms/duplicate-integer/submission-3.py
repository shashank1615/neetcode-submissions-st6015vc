class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashval = {}
        for val in nums:
            if val in hashval:
                return True;
            else:
                hashval[val] = 1;
        return False
        