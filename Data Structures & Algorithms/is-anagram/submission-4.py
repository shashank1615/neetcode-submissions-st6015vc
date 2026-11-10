class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        if len(s) == len(t):
            for i in range(0, len(s)):
                if s[i] in hash1:
                    hash1[s[i]] += 1
                else:
                    hash1[s[i]] = 1
            for i in range(0, len(t)):
                if t[i] in hash2:
                    hash2[t[i]] += 1
                else:
                    hash2[t[i]] = 1
            if hash1 == hash2:
                return True
        return False
                
            
        