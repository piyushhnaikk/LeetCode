class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        cur = 0
        seen = {}
        while cur != len(s):

            if s[cur] in seen:
                if seen[s[cur]] >= start:
                    start = seen[s[cur]] + 1
                
            
            seen[s[cur]] = cur

            if cur - start + 1 > longest:
                longest = cur - start + 1
            
            cur += 1

        return longest