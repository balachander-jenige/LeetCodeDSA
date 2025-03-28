class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res=[]
        n=len(nums)
        nums=sorted(nums)
        for i in range(n//2):
            res.append((nums[i]+nums[n-1-i])/2)
        return len(set(res))



        