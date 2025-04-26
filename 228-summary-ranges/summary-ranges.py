class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=[]
        i=0
        while i<len(nums):
            first=nums[i]
            while(  i<len(nums)-1 and nums[i]==nums[i+1]-1 ):
                i+=1
            end=nums[i]
            if first==end:
                l.append(f"{first}")
            else:
                l.append(f"{first}->{end}")
            i+=1
        return l        
        

        