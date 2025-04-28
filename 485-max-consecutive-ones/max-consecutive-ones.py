class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmpc=0
        maxc=0
        for i in range(len(nums)):
            if nums[i]==1:
                tmpc+=1
            if nums[i]==0 or i==len(nums)-1 :

                if tmpc > maxc :
                    maxc=tmpc
                tmpc=0   
        return maxc





        