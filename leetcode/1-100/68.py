class Solution:
	def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
		lines = []
		p = 0
		n = len(words)
		while p < n:
			curWidth = 0
			lines.append([])
			line = lines[-1]
			while p < n:
				w = words[p]
				space = 1 if len(line) > 0 else 0
				newWidth = curWidth + space + len(w)
				if newWidth > maxWidth:
					break
				curWidth = newWidth
				line.append(w)
				p += 1
			if len(line) == 0:
				return # We'll get stuck on this word

		def justifyLine(l):
			s = len(l) - 1
			spacesToAdd = maxWidth - len(''.join(l))
			if s == 0:
				return l[0] + ' '*spacesToAdd
			overflow = spacesToAdd % s
			pergap = int((spacesToAdd / s))
			justified = []
			for w in l[:-1]:
				justified.append(w)
				spaces = pergap + 1 if overflow > 0 else pergap
				overflow -= 1
				justified.append(' '*spaces)
			justified.append(l[-1])
			return ''.join(justified)


		for i in range(len(lines) - 1):
			lines[i] = justifyLine(lines[i])
		lastline = ' '.join(lines[-1])
		lines[-1] = lastline + ' '*(maxWidth - len(lastline))
		return lines
