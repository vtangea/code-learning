class Solution:
	def minWindow(self, s: str, t: str) -> str:
		l, r = 0, 0
		n = len(s)
		count = {}
		countsLeft = 0
		best = [0, 0]
		for c in t:
			if c not in count:
				count[c] = 0
				countsLeft += 1
			count[c] += 1
		while r < n:
			c = s[r]
			if c in count:
				count[c] -= 1
				if count[c] == 0:
					countsLeft -= 1
			while l <= r and countsLeft == 0:
				bestLen = best[1]-best[0]
				if bestLen == 0:
					best = [l, r+1]
				else:
					if r-l+1 < bestLen:
						best = [l, r+1]
				cl = s[l]
				if cl in count:
					count[cl] += 1
					if count[cl] == 1:
						countsLeft += 1
				l += 1
			r += 1

		return s[best[0]:best[1]]
