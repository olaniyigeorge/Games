import random

class GameState():
    def __init__(self, state=None):
        if state:
            self.state = state
        else:
            data= []
            tile_numbers= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            for row in range(4):
                xrow = []
                for tile in range(4):
                    choice= random.choice(tile_numbers)
                    xrow.append(choice)
                    tile_numbers.remove(choice)
                data.append(xrow)
            self.state = data


    def __str__(self):
        return f'Raw: {self.state}'
    
    def show(self):
        for row in self.state:
            for tile in row:
                print(f' {tile} ', end="")
            print()

    def get_empty(self):
        for row in self.state:
            for tile in row:
                if tile == 0:
                    return (self.state.index(row), row.index(tile))
    
    def is_arranged(self):
        goal = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]    
        ]
        if self.state == goal:
            return True
        else:
            return False
    
    def move_is_valid(self, move):
        x,y = move
        print(move)
        print(x)
        print(y)
        if 0 > x or x >3:
            # raise ValueError("Invalid move")
            return False
        if 0 > y or y > 3:
            # raise ValueError("Invalid move")
            return False
        
        return True
        
    
    ## Game Moves
    def up(self):
        '''
        Switches position of the empty tile with the one above it
        '''
        zero_tile = self.get_empty()
        zero = self.state[zero_tile[0]][zero_tile[1]]

        upper_tile = (zero_tile[0]-1, zero_tile[1])
        if self.move_is_valid(upper_tile):
            upper = self.state[upper_tile[0]][upper_tile[1]]        
        else:
            print('Invalid UP move ')
            return False
        
        self.state[upper_tile[0]][upper_tile[1]] = zero
        self.state[zero_tile[0]][zero_tile[1]] = upper
        return (f'UP: Switched {zero_tile}({zero}), for {upper_tile}({upper})')
    
    def down(self):
        '''
        Switches position of the empty tile with the one below it
        '''
        zero_tile = self.get_empty()
        zero = self.state[zero_tile[0]][zero_tile[1]]
        
        lower_tile = (zero_tile[0]+1, zero_tile[1])
        if self.move_is_valid(lower_tile):
            lower = self.state[lower_tile[0]][lower_tile[1]]
        else:
            print('Invalid DOWN move ')
            return False

        self.state[lower_tile[0]][lower_tile[1]] = zero
        self.state[zero_tile[0]][zero_tile[1]] = lower

        return (f'DOWN: Switched {zero_tile}({zero}), for {lower_tile}({lower})')

    def right(self):
        '''
        Switches position of the empty tile with the one by it's right 
        '''
        zero_tile = self.get_empty()
        zero = self.state[zero_tile[0]][zero_tile[1]]
        
        right_tile = (zero_tile[0], zero_tile[1]+1)
        if self.move_is_valid(right_tile):
            right = self.state[right_tile[0]][right_tile[1]]
        else:
            print('Invalid RIGHT move ')
            return False

        self.state[right_tile[0]][right_tile[1]] = zero
        self.state[zero_tile[0]][zero_tile[1]] = right

        return (f'RIGHT: Switched {zero_tile}({zero}), for {right_tile}({right})')
    
    def left(self):
        '''
        Switches position of the empty tile with the one by it's left 
        '''
        zero_tile = self.get_empty()
        zero = self.state[zero_tile[0]][zero_tile[1]]
        
        left_tile = (zero_tile[0], zero_tile[1]-1)
        if self.move_is_valid(left_tile):
            left = self.state[left_tile[0]][left_tile[1]]
        else:
            print('Invalid LEFT move ')
            return False


        self.state[left_tile[0]][left_tile[1]] = zero
        self.state[zero_tile[0]][zero_tile[1]] = left

        return (f'LEFT: Switched {zero_tile}({zero}), for {left_tile}({left})')
    
# Refactor
class GameCycle():

    def __init__(self, data,  next=None, parent=None):
        self.data = data
        self.parent = parent
        self.next = next

class GameMoves():

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = GameCycle(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def display(self):
        pass



class Puzzle():
    print("                  Welcome              ")
    print("                    to                 ")
    print("           FIFTEEN SQUARE PUZZLE       ")

    print("Controls: \n To move up, press: U \n To move down, press: D \n To move left, press: L \n To move right, press: R")
    print()
    print()

    def __init__(self):
        if not reversed:
            self.goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        else:
            self.goal = [[0,15,14,13,],[12,11,10,9],[8,7,6,5],[4,3,2,1]]
        
        self.states = GameMoves()
        self.start_config = None
        self.solved = False

    def shuffled_board(self):
        '''
        Generates a shuffled board relative to the goal
        '''
        board= []
        tile_numbers= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        shuffled= False
        while not shuffled:
            for row in range(4):
                xrow = []
                for tile in range(4):
                    choice= random.choice(tile_numbers)
                    xrow.append(choice)
                    tile_numbers.remove(choice)
                board.append(xrow)
            if board != self.goal:
                shuffled = True
        return board
    

    def play(self):
        self.start_config = self.shuffled_board()
        # self.states.append(start_config)

        while not self.solved:
            # Get the last state
            current = self.get_last_state()
            
            # get_possible_valid_moves
            # get_valid_input
            # apply_move
            # add result of a applying move and the valid_input to self.gamecycles {move: move, state: boardstate}
            # if result of a applying move is arranged
                # set self.solved to True
            # Add make resultin boardstate a direct child of current
            # display last state
        
            pass

    def get_possible_valid_moves(self, boardstate):
        '''
        :params: boardstate -- list of lists with 4 x 4 config
        :return: list
        Takes a board state and returns a list of possible valid moves
        ('U' | 'D' | 'L' | 'R) returns a list of all or some of these strings
        '''
        pass

    def get_valid_input(self, valid_moves, input):
        '''
        :params: valid_moves -- list of strings
        :params: input -- string
        :return: string
        Takes a list of valid moves(list of strings) and checks if input is in the list
        If input not in list, keep prompting for valid input else return input'''
        pass

    def apply_move(self, move, boardstate):
        '''
        :params: move -- string
        :params: boardstate -- list of lists with 4 x 4 config
        :return: list of lists with 4 x 4 config
        Takes a move and apply to the boardstate then returns a new boardstate
        '''
        pass

    def get_empty(self, boardstate):
        '''
        :params: boardstate -- list of lists with 4 x 4 config
        :return: tuple
        Takes a boardstate then returns a tuple(coordinate of the position of 0 in the board)
        '''
        pass
    
    
    # Game transition will be a (action, config) pair
        ## ('u', [[...],[...],[...],[...]])

    # u1-u2-u3-null4
    # 1
    def get_last_state(self):
        '''
        Takes the head of a linkedlist(start_config) and returns the youngest node(recent game cycle)
        '''
        current = self.start_config
        while current.next_node:
            current = current.next_node
            if current.next_node == None:
                return current
        return current
        












# # GAME PLAY
# def play():
#     print("                  Welcome              ")
#     print("                    to                 ")
#     print("           FIFTEEN SQUARE PUZZLE       ")

#     print("Controls: \n To move up, press: U \n To move down, press: D \n To move left, press: L \n To move right, press: R")

#     moves = []
#     game_states = []

#     start_state = GameState()
#     game_states.append(start_state)

#     while not start_state.is_arranged():
#         current_state = start_state
#         current_state.show()

#         move = input('Make your move...')
#         moves.append(move)
#         if make_move(move, current_state) == None:
#                 continue
        
#         current_state.show
#         game_states.append(current_state)
        


#     def make_move(move, state):
#         if move.lower('u'):
#             if not state.up():
#                 return None
              
#         elif move.lower('d'):
#             if not state.down():
#                 return None
#         elif move.lower('l'):
#             if not state.left():
#                 return None
#         elif move.lower('r'):
#             if not state.right():
#                 return None
#         else:
#             print("Invalid move")
#             return None


#     return None

# def train():
#     return None

# def play_with_AI():
#     return None



# play()