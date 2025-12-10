class Solution {
public:
    int removeDuplicates(vector<int>& a) {

        int i=0,j=0;
        int k=a.size();
        while(j<k){
            while(a[i]!= a[j]){
                i+=1;
                a[i]=a[j];
            }
            j+=1;
        }
        return i+1;       
    }
};