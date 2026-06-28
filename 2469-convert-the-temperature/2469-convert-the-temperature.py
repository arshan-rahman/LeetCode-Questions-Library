class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        kel=celsius+273.15
        far=celsius*1.80+32.00
        ans.append(kel)
        ans.append(far)
        return ans
        