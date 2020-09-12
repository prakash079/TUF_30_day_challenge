#question-link=https://leetcode.com/problems/sort-colors/
#topic=ARRAYS
----------------------------------------------------------------------
#solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 2:
				#  switch it to the tail
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] == 0:
				#  switch it to the head
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                if i > j: j = i # force j to be at least i
            elif nums[j] == 1:
                j += 1 # move on
        
