class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for x in range(9)]
        cols = [{} for x in range(9)]
        buckets = [{} for x in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] is ".":
                    continue
                n = int(board[i][j])
                if n < 0 or n > 9:
                    return False

                if n in rows[i]:
                    return False
                rows[i][n] = True

                if n in cols[j]:
                    return False
                cols[j][n] = True

                b = int(i/3) + 3*int(j/3)
                if n in buckets[b]:
                    return False
                buckets[b][n] = True
        return True
