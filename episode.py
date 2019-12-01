import game
import collections
import math
import state_action
import random
import q

PLAY_RANDOM = True

class Episode:
    def __init__(self):
        self.state_action_hashes = []
        self.board_history = []
        self.final_board = None
        self.result = 0

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
            return e
        
        if PLAY_RANDOM:
            p2_action = pick_random_action() 
            game_status = b.move(p2_action, 2)

            if game_status == 'Illegal':
                while game_status == 'Illegal':
                    p2_action = pick_random_action()
                    game_status = b.move(p2_action, 2)
        else:
            game_status, p2_action = q.play_best(b, 2)

        move_count += 1
        if (game_status == 'Win' or game_status == 'Tie' or game_status == 'Loss'):
            e.result = game_status
            return e
        
    return None

if __name__ == "__main__":
    win_count = 0
    q.load_q('Q')
    for i in range(0, 10000000):
        episode = generate_episode()
        if (episode.result == 'Win'):
            win_count += 1
        
        q.update_q_from_episode(episode)
        if (i >= 10000 and i % 10000 == 0):
            print(i, 'Win Rate: %', round((win_count / i) * 100, 1), '    StateAction Pairs: ', len(q.Q))
            print('Q Found Count:', q.q_found_count, 'Q Not Found Count:', q.q_notfound_count)
            if i % 100000 == 0:
                q.save_q('Q')
                print('Q Saved')


