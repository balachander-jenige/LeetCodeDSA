class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        Nom=0
        t=[]
        n=len(dist)
        for i in range(n):
            t.append(dist[i]/speed[i])
        t.sort()
        for i in range(n):
            if (t[i]-i)>0:
                Nom+=1
                print(Nom)
            else:
                break        
        return Nom
