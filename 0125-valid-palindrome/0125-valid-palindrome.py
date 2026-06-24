class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(char for char in s if char.isalnum())
        s2=s1.lower()
        revs=s2[::-1]
        if len(s2)==len(revs):
            if s2==revs:
                return True
            else:
                return False
        else:
            return False
        