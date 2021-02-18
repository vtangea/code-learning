class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		ans = []
		def branchOut(s, l, r):
			if l == n and r == n:
				ans.append(s)
				return
			if l > n or r > n or r > l:
				return
			branchOut(s + '(', l+1, r)
			branchOut(s + ')', l, r+1)
		branchOut('', 0, 0)
		return ans
