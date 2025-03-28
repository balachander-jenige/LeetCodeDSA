class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        res=[]
        for num in nums1:
            if num in nums2 or num in nums3:
                res.append(num)
        for num in nums2:
            if num in nums3 or num in nums1:
                res.append(num)
        return list(set(res))
       

        