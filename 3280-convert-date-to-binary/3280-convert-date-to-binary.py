class Solution:
    def convertDateToBinary(self, date: str) -> str:
        calen="-".join(f"{int(x):b}" for x in date.split("-"))
        return calen
        