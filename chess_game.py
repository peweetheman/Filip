
class board():
    def __init__(self):
        self.board_state = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                            ['P' for i in range(8)],
                            [" " for i in range(8)],
                            [" " for i in range(8)],
                            [" " for i in range(8)],
                            [" " for i in range(8)],
                            ['P' for i in range(8)],
                            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

    def print_board(self):
        for i in range(len(self.board_state)):
            row = self.board_state[i]
            print()
            print(i+1, end=" ")
            for piece in row:
                print(piece, end =" ")
        print()
        print('  A B C D E F G H')

    def do_move(self, init_pos_row, init_pos_col, final_pos_row, final_pos_col):
        print(init_pos_row, init_pos_col, final_pos_row, final_pos_col)
        if not self.is_legal(init_pos_row, init_pos_col, final_pos_row, final_pos_col):
            print("TRY AGAIN ILLEGAL MOVE")
            return
        self.board_state[final_pos_row][final_pos_col] = self.board_state[init_pos_row][init_pos_col]
        self.board_state[init_pos_row][init_pos_col] = " "

    def is_legal(self, init_pos_row, init_pos_col, final_pos_row, final_pos_col):
        piece = self.board_state[init_pos_row][init_pos_col]
        if piece == " ":
            return False
        if piece == "R":
            if not (init_pos_col == final_pos_col or init_pos_row == final_pos_row
                    and not (init_pos_col == final_pos_col and init_pos_row == final_pos_row)): # havent just stayed in the same square
                return False
            for i in range(init_pos_row, final_pos_row):
                for j in range(init_pos_col, final_pos_col):    # check for blockers
                    if self.board_state[i][j] != " ":
                        return False
        # continue writing out the legal moves for all pieces

my_board = board()
my_board.print_board()

not_over = True
while not_over:
    initial_column, initial_row = input("Enter initial column and row: ").split()
    final_column, final_row = input("Enter final column and row: ").split()
    initial_column = ord(initial_column.lower()) - 97
    initial_row = int(initial_row) - 1
    final_column = ord(final_column.lower()) - 97
    final_row = int(final_row) - 1
    my_board.do_move(initial_row, initial_column, final_row, final_column)
    my_board.print_board()