class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res={}
        finalres=[]
        for i in range(len(s)-10+1):
            if s[i:i+10] not in res:
                res[s[i:i+10]]=1
            else:
                res[s[i:i+10]]+=1
        print(res)
        for k,v in res.items():
            if v >1:
                finalres.append(k)
        return finalres
        