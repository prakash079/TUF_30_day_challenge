#question-link=https://leetcode.com/problems/find-the-duplicate-number/
#topic=ARRAY
------------------------------------------------------------------------------
#solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i+1]==nums[i]):
                return nums[i]
            
/*the basic idea behind this solution is first we can sort the array for eg:-array is=1,2,5,3,5,4 and the question states that we only have one repeating element in this array
so after sorting this :1,2,3,4,5,5 so now if we compare ith element with (i+1)th element then if they are same we got our element which is repeating*/

#TC = O(nlogn)
#space = O(1)
