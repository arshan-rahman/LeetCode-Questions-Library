from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq=Counter(str(n))
        score = 0
        for digit,count in freq.items():
            score+=int(digit)*count
        return score

        