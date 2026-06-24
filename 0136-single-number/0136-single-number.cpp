class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a = 0;
        int length = nums.size();

        for(int i = 0; i<length;i++){
            a = a ^ nums[i];
        }
        return a;
    }
};