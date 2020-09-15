#question-link=https://leetcode.com/problems/merge-intervals/

---------------------------------------------------------------------------
#solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged=[]
        if(len(intervals)==0):
            return merged
        intervals.sort()
        #print(intervals)
        l=intervals[0]
        for i in intervals:
            if(i[0]<=l[1]):
                l[1]=max(i[1],l[1])
            else:
                merged.append(l)
                l=i
        merged.append(l)
        return merged
