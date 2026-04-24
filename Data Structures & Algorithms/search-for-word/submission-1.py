class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        def dfs(i,r,c):
            if i == len(word):
                return True
            
            if r<0 or c<0 or r>=row or c>= col or board[r][c] != word[i] or board[r][c] == '#':
                return False
        
            board[r][c] = '#'

            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))

            return res

        for i in range(row):
            for j in range(col):
                if dfs(0,i,j):
                    return True
        return False