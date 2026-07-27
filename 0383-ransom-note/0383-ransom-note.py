class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = {}

        for i in range(len(magazine) ):
            if i < len(magazine):
                if magazine[i] in freq:
                    freq[magazine[i]] += 1
                else:
                    freq[magazine[i]] = 1
        for i in range(len(ransomNote)):

            if i < len(ransomNote):
                if ransomNote[i] in freq:
                    freq[ransomNote[i]] -= 1
                else:
                    freq[ransomNote[i]] = -1

        return not any(v < 0 for v in freq.values())


            