class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        return max(hashmap, key=hashmap.get)
        