class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr1=[]
        for i in range(1,n+1):
            if i%m!=0:
                arr1.append(i)
        arr2=[]
        for i in range(1,n+1):
            if i%m==0:
                arr2.append(i)
        return sum(arr1) - sum(arr2)