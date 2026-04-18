class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def issafe(r, c):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for c in range(n):
                if issafe(row, c):
                    board[row][c] = "Q"
                    backtrack(row + 1)
                    board[row][c] = "."

        backtrack(0)
        return res
