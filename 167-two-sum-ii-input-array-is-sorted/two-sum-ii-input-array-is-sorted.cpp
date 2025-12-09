class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int res) {
        int i=0,sum=0;
        int j=nums.size()-1;
        while(i<j){
            sum=nums[i]+nums[j];
            if (sum>res){
                j-=1;
            }else if(sum<res){
                i+=1;
            }
            else{
                return {i+1,j+1}; 
            }

        }
        return {-1,-1};
    }
};