import game
import collections
import math
import state_action
import random
import q

class Episode:
    def __init__(self):
        self.state_action_hashes = []
        self.board_history = []
        self.result = 0

def pick_random_action():
    return random.randint(0, 6)

def generate_episode():
    e = Episode()
    b = game.Board()
    while True:
        p1_action = q.pick_best_action(b) # TODO invalid eklemesi
        game_status = b.move(p1_action, 1)
        sah = state_action.get_hash_from_board(b, p1_action)
        e.state_action_hashes.append(sah)

        if (game_status == 'Win' or game_status == 'Tie' or game_status == 'Loss'):
            e.result = game_status
            return e
        
        p2_action = pick_random_action() # TODO invalid eklemesi
        game_status = b.move(p2_action, 2)

        if (game_status == 'Win' or game_status == 'Tie' or game_status == 'Loss'):
            e.result = game_status
            return e
        
    return None

if __name__ == "__main__":
    win_count = 0
    for i in range(0, 1000000):
        episode = generate_episode()
        if (episode.result == 'Win'):
            win_count += 1
        
        q.update_q_from_episode(episode)
        print(win_count, i)


