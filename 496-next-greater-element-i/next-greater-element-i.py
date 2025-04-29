class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            m=i
            a=-1
            elementindex=nums2.index(m)
            for j in range(elementindex,len(nums2)):
                if nums2[j]>m:
                    a=nums2[j]
                    break
            ans.append(a)
        return ans      
            
         
        return res  