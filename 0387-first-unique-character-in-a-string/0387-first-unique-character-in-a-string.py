class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = 0
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        

        for i in s:

            if freq[i] == 1:
                return index
            
            index += 1
        
        return -1