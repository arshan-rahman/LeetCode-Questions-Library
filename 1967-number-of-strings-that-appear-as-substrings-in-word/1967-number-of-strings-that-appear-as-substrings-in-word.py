class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        count=0
        for pots in patterns:
            if pots in word:
                count+=1
        return count
        