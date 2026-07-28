class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str_s = 0
        str_t = 0

        while(str_s < len(s) and str_t < len(t)):
            
            if s[str_s] == t[str_t]:
                str_s += 1
                str_t += 1


            elif s[str_s] != t[str_t]:
                str_t += 1
            
        return str_s > len(s)-1
        
       
        