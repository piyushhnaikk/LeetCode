class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ = 0
        t_ = 0

        while s_ < len(s) and t_ < len (t):
            if s[s_] == t[t_]:
                s_ += 1
            t_ += 1
        return s_ > len(s) - 1