class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        digit=str(digit)
        count = 0
        for num in nums:
            count += str(num).count(digit)
        return count