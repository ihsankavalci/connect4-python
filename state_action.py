Player1 = 1
Player2 = 2

def get_hash_from_board(state, action):
    s = 0
    for i in range(state.rows):
        for j in range(state.cols):
            k = (i * state.cols + j) % 64
            if (state.board[i][j] == Player1 or state.board[i][j] == 0) == True:
                m = 0
            else:
                m = 1
            v = (m << k)
            s = s | v
    
    value = (s << 4) + action
    return value

# class StateAction():
#     def __init__(self, s, a):
#         self.state = s
#         self.action = a

#     def get_hash(self):
#         s = 0
#         a = self.action
#         for i in range(self.state.rows):
#             for j in range(self.state.cols):
#                 k = (i * self.state.cols + j) % 64
#                 if (self.state.board[i][j] == Player1 or self.state.board[i][j] == 0) == True:
#                     m = 0
#                 else:
#                     m = 1
#                 #m = (self.state.board[i][j] == Player1 or self.state.board[i][j] == 0) ? 0 : 1
#                 v = (m << k)
#                 s |= v
            
#         return (s << 4) + a