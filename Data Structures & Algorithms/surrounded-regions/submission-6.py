class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.safe = set()
        self.visited = set()
        rows = len(board)
        cols = len(board[0])
        top = 0
        bottom = len(board) - 1
        left = 0
        right = cols - 1

                
        def safe_dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or (row, col) in self.visited or board[row][col] == 'X':
                return
            
            self.safe.add((row, col))
            self.visited.add((row, col))
            safe_dfs(row - 1, col)
            safe_dfs(row + 1, col)
            safe_dfs(row, col - 1)
            safe_dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if board[top][col] == 'O':
                    self.safe.add((top, col))
                    safe_dfs(top, col)
                if board[bottom][col] == 'O':
                    self.safe.add((bottom, col))
                    safe_dfs(bottom, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][left] == 'O':
                    self.safe.add((row, left))
                    safe_dfs(row, left)
                if board[row][right] == 'O':
                    self.safe.add((row, right))
                    safe_dfs(row, right)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    if ((row, col)) not in self.safe:
                        board[row][col] = 'X'
        



        
        