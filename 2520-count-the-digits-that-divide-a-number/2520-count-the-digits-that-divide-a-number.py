class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        lst = list(map(int, str(num)))
        for i in range(len(lst)):
            if num%lst[i]==0:
                count+=1
        return count
        