import numpy as np
import pygame

ROW_COUNT = 6
COLUMN_COUNT = 7
class Board():
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = np.zeros((6,7))
    
    def move(self, action, player):
        if (self.board[0][action] != 0):
            return 'Illegal'
        for i in range(self.rows - 1, -1, -1):
            if (self.board[i][action] == 0):
                self.board[i][action] = player
                #changed_row = i
                return self.check_result(player)
                
    
    def check_result(self, player):
        # Check tie
        filled_count = 0
        for i in range(0, self.cols):
            if self.board[0][i] != 0:
                filled_count += 1
        if filled_count == self.cols:
            return 'Tie'

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

class Visual():
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0) 
    SQUARESIZE = 100
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, self.BLUE, (c*self.SQUARESIZE, r*self.SQUARESIZE+self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, self.BLACK, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, self.RED, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int((ROW_COUNT-1-r)*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(self.screen, self.YELLOW, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int((ROW_COUNT-1-r)*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        pygame.display.update()

    def __init__(self):
        pygame.init()
        

        size = (self.width, self.height)
        self.RADIUS = int(self.SQUARESIZE/2 - 5)
        self.screen = pygame.display.set_mode(size)
        #draw_board(b.board)
        #pygame.display.update()
        #myfont = pygame.font.SysFont("monospace", 75)

    