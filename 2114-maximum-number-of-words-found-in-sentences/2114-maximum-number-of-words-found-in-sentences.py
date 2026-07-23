class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
     wcount=[]
     for i in range(len(sentences)):
        count=len(sentences[i].split())
        wcount.append(count)
     return max(wcount)
        
        
        
        