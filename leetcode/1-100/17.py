from collections import deque
class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if len(digits) == 0:
			return []
		letters = [{}, {},
			{'a','b','c'},
			{'d','e','f'},
			{'g','h','i'},
			{'j','k','l'},
			{'m','n','o'},
			{'p','q','r','s'},
			{'t','u','v'},
			{'w','x','y','z'}
		]
		def letterCombos(dgs, i):
			ans = []
			if len(dgs) - i == 0:
				return [deque()]
			cands = letterCombos(dgs, i+1)
			c = int(dgs[i])
			for cand in cands:
				for l in letters[c]:
					item = deque(cand)
					item.appendleft(l)
					ans.append(item)
			return ans
		ans = letterCombos(digits, 0)
		for i in range(len(ans)):
			ans[i] = ''.join(ans[i])
		return ans
