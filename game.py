import numpy as np

class Board():
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = np.zeros((6,7))
    
    def move(self, action, player):
        if (self.board[0][action] != 0):
            return 'Illegal'
        for i in range(self.rows - 1, 0, -1):
            if (self.board[i][action] == 0):
                self.board[i][action] = player
                #changed_row = i
                return self.check_result(player)
                
    
    def check_result(self, player):
        # Check horizontal locations for win
        end = False
        for c in range(self.cols-3):
            for r in range(self.rows):
                if self.board[r][c] == player and self.board[r][c+1] == player and self.board[r][c+2] == player and self.board[r][c+3] == player:
                    end = True
        
        # Check vertical locations for win
        for c in range(self.cols):
            for r in range(self.rows-3):
                if self.board[r][c] == player and self.board[r+1][c] == player and self.board[r+2][c] == player and self.board[r+3][c] == player:
                    end = True
                
        # Check positively sloped diaganols
        for c in range(self.cols-3):
            for r in range(self.rows-3):
                if self.board[r][c] == player and self.board[r+1][c+1] == player and self.board[r+2][c+2] == player and self.board[r+3][c+3] == player:
                    end = True

        # Check negatively sloped diaganols
        for c in range(self.cols-3):
            for r in range(3, self.rows):
                if self.board[r][c] == player and self.board[r-1][c+1] == player and self.board[r-2][c+2] == player and self.board[r-3][c+3] == player:
                    end = True
        
        if (end):
            if (player == 1):
                return 'Win'
            elif (player == 2):
                return 'Loss'
        
        else:
            return 'Intermediate'