class Solution:
    def mirrorDistance(self, n: int) -> int:
        sn=str(n)
        rev=sn[::-1]
        n2=int(rev)
        return abs(n2-n)
        