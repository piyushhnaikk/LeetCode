class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k - 1
        vowels = 0
        for i in range (k):
            if s[i] in "aeiou":
                vowels += 1

        max_vowels = vowels
        while right + 1 < len(s):
            
            right += 1

            if s[left] in "aeiou" :
                vowels -= 1
            
            if s[right] in "aeiou" :

                vowels += 1
            
            left += 1
            
            if vowels > max_vowels:
                max_vowels = vowels
        return max_vowels