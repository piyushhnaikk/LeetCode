class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        reflects = {}
        reflectt = {}

        if len(s) != len(t):
            return False
        else:
            for i in range (len(s)):
                if s[i] in reflects:
                    if reflects[s[i]] == t[i]:
                        continue
                    
                    else:
                        return False
                
                else:
                    reflects[s[i]] = t[i]
                if t[i] in reflectt:
                    if reflectt[t[i]] == s[i]:
                        continue
                    
                    else:
                        return False
                
                else:
                    reflectt[t[i]] = s[i]
        
        return True