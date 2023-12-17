class Board : 
    def __init__(self, board_size) :
        self.board_size = board_size
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board[0][0] = 1

Chessboard = Board(8)