class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        int n=nums.size();
        for (int i=0;i<n-2;i++){
            if(i>0 and nums[i]==nums[i-1]){
                continue;
            }
            int left=i+1;
            int right=nums.size()-1;
            while(left < right){
                int total =nums[i]+nums[left]+nums[right];
                if (total ==0){
                    res.push_back({nums[i],nums[left],nums[right]});

                    left+=1;
                    right-=1;
                    while(left<n && nums[left]==nums[left-1] )
                    {
                        left+=1;
                    }
                    while(right>0 && nums[right]==nums[right+1])
                    {
                        right--;
                    }
                }
                else if(total < 0){
                       left++;

                }
                else{
                    right--;
                }
            }
            
        }

        return res;
            
        

                 
    }
};