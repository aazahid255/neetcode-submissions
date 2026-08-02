# input: 2-d grid of characters, and a string word
# output: true if word exists, false if it doesnt
# edge cases: empty board, 1xn, nx1 board, uppercase or loewrcase, going past boundaries

# match: backtracking

# plan: 
# base cases: if we have reached length of word in our path, and it is the same, we can return True
# if the current index is equal to the index at word, then we can start exploring 
# so we should have a "path" that acts as our string, and an index for comparison pruposes
# if the index at current path is equal to the index at word, we can add it to our path and continue searching
# if it isnt, we want to go back and search other possiblities
# once our index is past the final index of board, we have to return false as a base case
# we can get len{board} by getting length of one row * col
# so the plan is to know the length of the bnoard
# we have a recursive backtrack helper
# there r 2 base cases: if index > len(board), which we would return false
# if len(path) == len(word, we return true)

# if index (start at 0) is equal to index (0) of word, we can start backtracking into horizional and vertical spaces. set up conditoinals to make sure these exist (get len board)
# if the index at this point isnt equal, we return. this is our backtrakc. make this the very first base case

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.len_col = len(board[0])
        self.len_row = len(board)
        self.path = set()

        def backtrack(i, row, col):
            if i == len(word):
                return True
            if (col >= self.len_col or row >= self.len_row or col < 0 or row < 0 or (row, col) in self.path or word[i] != board[row][col]):
                return False

            self.path.add((row, col))
            res = backtrack(i + 1, row + 1, col) or backtrack(i + 1, row, col + 1) or backtrack(i + 1, row - 1, col) or backtrack(i + 1, row, col - 1) 
            self.path.remove((row,col))
            return res

        for r in range(self.len_row):
            for c in range(self.len_col):
                if backtrack(0, r, c) == True:
                    return True
        return False


    
                
                
                
                # we do len(path) to figure out where we are in the pathrn
                 # im pretty sure y_coord reps the first thing, bc board[3][0] would be the A in the 3rd row
        