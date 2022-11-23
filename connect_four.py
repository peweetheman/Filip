class board():
    def __init__(self):
        pass
        # make 2D list to represent 'R' 'B'
    def print_board(self):
        pass
    def do_move(self, column_number):
        pass

my_board = board()
my_board.print_board()

not_over = True
while not_over:
    move_column = input("Enter column: ")
    my_board.do_move(move_column)
    my_board.print_board()