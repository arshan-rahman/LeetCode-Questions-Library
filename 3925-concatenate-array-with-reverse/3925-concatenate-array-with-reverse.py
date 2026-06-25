class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev=nums[::-1]
        ans=nums+rev
        return ans
        