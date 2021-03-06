import random
import math
import state_action
import pickle

WIN_WEIGHT = 1.0
TIE_WEIGHT = 0.0
LOSS_WEIGHT = -1.0
GAMMA = 0.5
SPLIT = .99

Q = {}
Q_Count = {}

q_found_count = 0
q_notfound_count = 0

def update_q(sah, ret):
    global q_found_count, q_notfound_count
    #sah = state_action.get_hash() # state action hash
    if Q.get(sah):
        Q[sah] = (Q_Count[sah] * Q[sah] + ret)/(Q_Count[sah] + 1)
        Q_Count[sah] = Q_Count[sah]+1
        q_found_count += 1
    else:
        Q[sah] = ret
        Q_Count[sah] = 1
        q_notfound_count += 1

def update_q_from_episode(episode):
    i = 0
    #print('EPISODE LEN:', len(episode.state_action_hashes))
    for state_action in episode.state_action_hashes:
        weight = 0.0
        if (episode.result == 'Win'):
            weight = WIN_WEIGHT
        elif (episode.result == 'Loss'):
            weight = LOSS_WEIGHT
        elif (episode.result == 'Tie'):
            weight = TIE_WEIGHT

        futureDiscountedReturn = weight * math.pow(GAMMA, i)
        update_q(state_action, futureDiscountedReturn)
        i+=1

def get_random_weight():
    return round(random.uniform(0.0, 0.1), 3)

def pick_random(probs):
    u = sum(i[1] for i in probs)
    r = round(random.uniform(0.0, u), 3)
    s = 0
    for t in probs:
        s = s + t[1]
        if (r <= s):
            return t[0]
    
    print('ERROR PICK RANDOM')
    return -1 # error



def pick_best_action(board, illegal_count):
    best_column = 0
    best_weight = 0
    leftover = ((1.0 - SPLIT) / (board.cols - 1))
    #probs = []
    for i in range(0, board.cols):
        sah = state_action.get_hash_from_board(board, i)
        weight = get_random_weight()
        if (Q.get(sah)):
            weight = Q[sah]
        
        if (weight > best_weight):
            best_column = i
            best_weight = weight
        
        #probs.append((i, weight))
    
    # probs = sorted(probs, key=lambda tup: tup[1], reverse=True)
    # return probs[illegal_count][0]

    probs = []
    for i in range(0, board.cols):
        if (i == best_column):
            probs.append((i, SPLIT))
        else:
            probs.append((i, leftover))
    
    return pick_random(probs)

def play_best(b, p):
    a = pick_best_action(b, 0)
    game_status = b.move(a, p)

    if game_status == 'Illegal':
        illegal_count = 1
        while game_status == 'Illegal':
            a = pick_best_action(b, illegal_count)
            game_status = b.move(a, p)
    return game_status, a

def save_q(filename):
    with open(filename + '.pkl', 'wb') as f:
        pickle.dump((Q, Q_Count), f, pickle.HIGHEST_PROTOCOL)

def load_q(filename):
    with open(filename + '.pkl', 'rb') as f:
        obj = pickle.load(f)
        global Q, Q_Count
        Q = obj[0]
        Q_Count = obj[1]