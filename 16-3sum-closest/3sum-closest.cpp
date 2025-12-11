class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int min=99999;
        sort(nums.begin(),nums.end());
        int res=0;
        for (int i=0;i<nums.size()-2;i++){
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            int l=i+1;
            int r=nums.size()-1;
            while(l<r)
            {
                int total=nums[i]+nums[l]+nums[r];
                if (min > abs(total-target))
                {
                min=abs(total-target);
                res=total;
                }
                if (total < target){
                           l++;

                }
                else
                {
                        r--;

                }
            }


            
        }

        return res;
        
    }
};