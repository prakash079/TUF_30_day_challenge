#question-link=https://leetcode.com/problems/merge-sorted-array/

---------------------------------------------------------------------
#solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums1:
            if i == 0:
                del nums1[m:len(nums1)]
        for i in nums2:
            nums1.append(i)
        x = sorted(nums1)
        for i in range(len(x)):
            nums1[i]=x[i]
              
        
            
