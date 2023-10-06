from fifteen_square_puzzle import GameState


goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0],
]

start = [
    [13, 4, 9, 7],
    [12, 11, 2, 8],
    [3, 0, 6, 15],
    [14, 1, 5, 10],
]

invalid_board = [
    [13, 4, 9, 7],
    [12, 11, 2, 8],
    [3, 2, 6, 15],
    [14, 1, 5, 10],
]

def get_empty(boardstate):
            '''
            :params: boardstate -- list of lists with 4 x 4 config
            :return: tuple
            Takes a boardstate then returns a tuple(coordinate of the position of 0 in the board)
            '''
            for row in boardstate:
                for item in row:
                    if item == 0:
                        return (boardstate.index(row), row.index(item)) 
            raise Exception('Invalid board config: Empty tile not found')

def validate_move(move, zero_coord):
        '''
        :params: move -- string
        :params: zero_coord -- a tuple. The coordinate of the empty tile
        :return: boolean
        Takes a move(a string) test if move is in a defined range of moves['U' | 'D' | 'L' | 'R]. 
        If not raise exception(Invalid move). 
        Check if the move and return either true or false 
        '''
        valid_moves = ['U', 'D', 'L', 'R']
        if move.upper() not in valid_moves:
            raise Exception("Invalid Move")

        if move.upper() == "U":
            result = (zero_coord[0]-1 , zero_coord[1])
        if move.upper() == "D":
            result = (zero_coord[0]+1 , zero_coord[1])
        if move.upper() == "L":
            result = (zero_coord[0] , zero_coord[1]-1)
        if move.upper() == "R":
            result = (zero_coord[0] , zero_coord[1]+1)
        
        for i in result:
            if i < 0 or i > 3:
                return False
        
        return True

def get_possible_valid_moves(boardstate):
        '''
        :params: boardstate -- list of lists with 4 x 4 config
        :return: list
        Takes a board state and returns a list of possible valid moves
        ('U' | 'D' | 'L' | 'R) returns a list of all or some of these strings
        '''
        # make a list a list of moves
        moves = ['U', 'D', 'L', 'R']
        # get the position on the empty space 
        try:
            empty_tile_coord = get_empty(boardstate)
        except Exception as e:
             print(e)
             exit()
        # validate the four moves
        for move in moves:
            # if any of the returns a number below 0 or above 3
            if not validate_move(move, empty_tile_coord):
                # remove that move from the valid moves list 
                moves.remove(move)
        # return the rest of the list(valid moves)
        return moves


def apply_move(move, boardstate):
        '''
        :params: move -- string
        :params: boardstate -- list of lists with 4 x 4 config
        :return: list of lists with 4 x 4 config
        Takes a move and apply to the boardstate then returns a new boardstate
        Does this by getting the position of the empty tile and switching with the one above, below, by the right or left of it.        
        '''
        zero_tile = get_empty(boardstate)
        zero = boardstate[zero_tile[0]][zero_tile[1]]

        # Validate move 
        if not validate_move(move, zero_tile):
            raise Exception("Invalid move")

        # Get coordinates of the tile to be moved
        if move.upper() == 'U':
            to_be_moved_coord = (zero_tile[0]-1, zero_tile[1])
        elif move.upper() == 'D':
            to_be_moved_coord = (zero_tile[0]+1, zero_tile[1])
        elif move.upper() == 'L':
            to_be_moved_coord = (zero_tile[0], zero_tile[1]-1)
        elif move.upper() == 'R':
            to_be_moved_coord = (zero_tile[0], zero_tile[1]+1)
        else:
            raise Exception('Invalid move')
        to_be_moved = boardstate[to_be_moved_coord[0]][to_be_moved_coord[1]]

        # Switch positions
        boardstate[to_be_moved_coord[0]][to_be_moved_coord[1]] = zero
        boardstate[zero_tile[0]][zero_tile[1]] = to_be_moved

        return boardstate

    
def main():
    for row in start:
         print(row)
    print()
    for row in apply_move('U', start):
        print(row)
    print()
    for row in apply_move('U', start):
        print(row)
    print()
    for row in apply_move('U', start):
        print(row)

# def main():
#     game = GameState(start)
#     print(game)
#     game.show()

#     print()
#     print(f"Empty tile is at {game.get_empty()}")
#     print()

#     print(game.up())
#     game.show()

#     print(game.left())
#     game.show()

#     print(game.left())
#     game.show()

#     print(game.down())
#     game.show()

#     print(game.right())
#     game.show()


 
if __name__ == "__main__":
    main()