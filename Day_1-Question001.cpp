//Question-link=https://leetcode.com/problems/sort-colors/
//this is more optimized solution

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n=nums.size();
        int low=0,mid=0,high=n-1;
        //for(int i=0;i<n;i++)
        while(mid<=high)
        {
            if(nums[mid]==0)
            {
                int t=nums[low];
                nums[low]=nums[mid];
                nums[mid]=t;
                low++;
                mid++;
            }
            else if(nums[mid]==1)
            {
                mid++;
            }
            else
            {
                int t=nums[high];
                nums[high]=nums[mid];
                nums[mid]=t;
                high--;
            }
        }
        
    }
};
