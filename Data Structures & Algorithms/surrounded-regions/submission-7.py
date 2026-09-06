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

        for col in range(cols):
            if board[0][col] == 'O': safe_dfs(0, col)
            if board[rows - 1][col] == 'O': safe_dfs(rows - 1, col)

        for row in range(rows):
            if board[row][0] == 'O': safe_dfs(row, 0)
            if board[row][cols - 1] == 'O': safe_dfs(row, cols - 1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    if ((row, col)) not in self.safe:
                        board[row][col] = 'X'
        



        
        