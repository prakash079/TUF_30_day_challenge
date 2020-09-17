#question-link=https://leetcode.com/problems/pascals-triangle/
_____________________________________________________________________________
class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		if numRows == 0:
			return []
		if numRows == 1:
			return [[1]]
		if numRows == 2:
			return [[1], [1,1]]
		base = [[1], [1,1]]
		for _ in range(numRows-2):
			next_one = [1]
			for i in range(len(base[-1])-1):              
				next_one.append(base[-1][i] + base[-1][i+1])
			next_one.append(1)
			base.append(next_one)
		return base
