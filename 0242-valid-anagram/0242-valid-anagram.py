class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s.lower())
        sort_t = sorted(t.lower())

        if len(sort_s) == len(sort_t):
            if sort_s == sort_t:
                return True
            else:
                return False
        else:
            return False