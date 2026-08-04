class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[]
        words=s.split()
        for word in words:
            res=word[::-1]
            arr.append(res)
        ans=" ".join(arr)
        return ans
        