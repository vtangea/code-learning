class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:
		out = set()
		def restore(idx, path, k):
			if k == 4:
				if idx >= len(s):
					out.add('.'.join(path))
				return
			if idx >= len(s):
				return
			k += 1
			restore(idx + 1, path + [s[idx:idx+1]], k)
			if s[idx] == '0': return
			restore(idx + 2, path + [s[idx:idx+2]], k)
			if int(s[idx:idx+3]) > 255: return
			restore(idx + 3, path + [s[idx:idx+3]], k)
		restore(0, [], 0)
		return list(out)
