import random




class GameState():
    def __init__(self, state):
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
            exit()
        
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
            exit()

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
            exit()

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
            exit()


        self.state[left_tile[0]][left_tile[1]] = zero
        self.state[zero_tile[0]][zero_tile[1]] = left

        return (f'LEFT: Switched {zero_tile}({zero}), for {left_tile}({left})')
    

