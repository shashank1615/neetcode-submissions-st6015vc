class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            result = ''.join(sorted(string))
            if result in hashmap:
                hashmap[result].append(string)  
            else:
                hashmap[result] = [string]
        return list(hashmap.values())