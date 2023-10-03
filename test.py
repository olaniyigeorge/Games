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






def main():
    game = GameState(start)
    print(game)
    game.show()

    print()
    print(f"Empty tile is at {game.get_empty()}")
    print()

    print(game.up())
    game.show()

    print(game.left())
    game.show()

    print(game.left())
    game.show()

    print(game.down())
    game.show()

    print(game.right())
    game.show()


 
if __name__ == "__main__":
    main()