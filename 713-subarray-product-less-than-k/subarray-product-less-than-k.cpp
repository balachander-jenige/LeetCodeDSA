class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k<=1){
            return 0;
        }
        int left=0;
        int count =0;
        int product=1;
         for (int r=0;r<nums.size();r++){
            product*=nums[r];
            while(product>=k)
            {
                product/=nums[left];
                left++;
            }
            count+=r-left+1;
         }
        return count;


    }
};