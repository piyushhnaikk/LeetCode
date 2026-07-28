class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_str = ""
        for i in s.lower():
            if ( 'a' <= i <= 'z') or ('0' <= i <= '9'):
                final_str += i
        return final_str == final_str[::-1]

        