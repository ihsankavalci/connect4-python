import game
import collections
import math
import state_action
import random
import q
import minimax
import time
import copy
import pygame

PLAY_RANDOM = False
MINIMAX_DEPTH = 5 # MAX 5

class Episode:
    def __init__(self):
        self.state_action_hashes = []
        self.board_history = []
        self.final_board = None
        self.result = 0
    
    def replay_episode(self):
        v = game.Visual()
        #print(self.board_history, len(self.board_history))

        for board in self.board_history:
            v.draw_board(board)
            v.update_display()
            pygame.event.get()
            time.sleep(1)

        v.draw_board(self.final_board)
        v.update_display()
        time.sleep(4.5)
        pygame.quit()

def pick_random_action():
    return random.randint(0, 6)

def generate_episode():
    e = Episode()
    b = game.Board()
    move_count = 0
    while True:
        if (move_count > 42):
            print('error move count')

        game_status, p1_action = q.play_best(b, 1)
        sah = state_action.get_hash_from_board(b, p1_action)
        e.state_action_hashes.append(sah)

        move_count += 1
        if (game_status == 'Win' or game_status == 'Tie' or game_status == 'Loss'):
            e.result = game_status
            e.final_board = b.board
            return e
        
        if PLAY_RANDOM:
            p2_action = pick_random_action() 
            game_status = b.move(p2_action, 2)

            if game_status == 'Illegal':
                while game_status == 'Illegal':
                    p2_action = pick_random_action()
                    game_status = b.move(p2_action, 2)
        else: # play with minimax
            converted_board = b.convert_board()
            m = minimax.Minimax(converted_board)
            p2_action = m.bestMove(MINIMAX_DEPTH, converted_board, 'o')
            game_status = b.move(p2_action[0], 2)

            if game_status == 'Illegal':
                print('Minimax ERROR')
                while game_status == 'Illegal':
                    p2_action = pick_random_action()
                    game_status = b.move(p2_action, 2)

        move_count += 1
        e.board_history.append(copy.deepcopy(b.board))
        if (game_status == 'Win' or game_status == 'Tie' or game_status == 'Loss'):
            e.result = game_status
            e.final_board = b.board
            return e
        
    return None

if __name__ == "__main__":
    win_count = 0
    q.load_q('Q')
    print_interval = 5
    save_interval = 20
    for i in range(0, 10000000):
        episode = generate_episode()
        if (episode.result == 'Win'):
            win_count += 1

        #episode.replay_episode()
        q.update_q_from_episode(episode)
        if (i >= print_interval and i % print_interval == 0):
            print(i, 'Win Rate: %', round((win_count / print_interval) * 100, 1), '    StateAction Pairs: ', len(q.Q))
            print('Q Found Count:', q.q_found_count, '      Q Not Found Count:', q.q_notfound_count)
            win_count = 0
            q.q_found_count = 0
            q.q_notfound_count = 0
            #episode.replay_episode()
            if i % save_interval == 0:
                q.save_q('Q')
                print('Q Saved')


