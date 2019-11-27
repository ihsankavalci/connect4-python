import pygame
import game
import math
import sys
import q
game_over = False
v = game.Visual()
b = game.Board()
v.draw_board(b.board)
turn = 1
q.load_q('Q')
game_status = 'Intermediate'
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(v.screen, v.BLACK, (0,0, v.width, v.SQUARESIZE))
            posx = event.pos[0]
            if turn == 2: 
                pygame.draw.circle(v.screen, v.YELLOW, (posx, int(v.SQUARESIZE/2)), v.RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(v.screen, v.BLACK, (0,0, v.width, v.SQUARESIZE))
            if turn == 2:
                posx = event.pos[0]
                col = int(math.floor(posx/v.SQUARESIZE))
                game_status = b.move(col, 2)
                v.draw_board(b.board)
                turn = 1
                print(game_status)
        pygame.display.update()
        
    if game_status == 'Win' or game_status == 'Tie' or game_status == 'Loss':
        input()
    if turn == 1:
        game_status, action = q.play_best(b, 1)
        v.draw_board(b.board)
        print(game_status)
        if game_status == 'Intermediate':
            turn = 2
    
