class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		if n <= 1:
			return
		N = n-1
		for l in range(int(n/2)):
			for i in range(l, N-l):
				tmp = matrix[l][i]
				matrix[l][i] = matrix[N-i][l]
				matrix[N-i][l] = matrix[N-l][N-i]
				matrix[N-l][N-i] = matrix[i][N-l]
				matrix[i][N-l] = tmp
