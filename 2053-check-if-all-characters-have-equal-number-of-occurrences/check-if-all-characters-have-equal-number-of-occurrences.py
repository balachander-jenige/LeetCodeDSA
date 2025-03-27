from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        

        d=defaultdict(int)
        for c in s:
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] +=1  
        res=list(set(d.values()))
        if len(res)!=1:
            return False
        return True
            
            



        