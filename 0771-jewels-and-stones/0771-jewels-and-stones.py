class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sets=set(jewels)
        count=0
        for stone in stones:
            if stone in sets:
                count+=1
        return count