from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        hashmap=defaultdict(int)
        for n in nums:
            hashmap[n]+=1
        for key,value in hashmap.items():
            if value >1:
                res.append(key)
        return res

        