class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        result = sorted(hashmap.items(), key = lambda pair: pair[1], reverse = True)
        return [item[0] for item in result[:k]]