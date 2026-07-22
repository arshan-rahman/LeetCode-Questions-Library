from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        running = 0

        for num in nums:
            running += num
            result.append(running)

        return result