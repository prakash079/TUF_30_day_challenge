#question-link=https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/

--------------------------------------------------------------------------------------
#solution
class Solution:
    def findTwoElement( self,l, n):
        ans=[0]*2
        k=list(set(l))
        ans[1]=((n*(n+1))//2)-sum(k)
        ans[0]=sum(l)-sum(k)
        return(ans)
#TC=o(n)
#space=o(n)

----------------------------------------------------------------------------------------------------
