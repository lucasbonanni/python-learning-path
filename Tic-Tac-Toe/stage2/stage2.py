class board:
    _width = 0
    _height = 0
    _x_count = 0
    _circle_count = 0
    _cells = []

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def print_frame_line(self):
        print('---------')

    def print_row(self, line):
        print('| ' + ' '.join(line) + ' |')

    def print_board(self):
        self.print_frame_line()
        for col in range(self._width - 1, -1, -1):
            self.print_row([self._cells[0][col], self._cells[1]
                            [col], self._cells[2][col]])
        self.print_frame_line()

    def initialize_board(self, cells):
        for row in range(0, self._width):
            self._cells.append(
                [cells[6 + row], cells[3 + row], cells[0 + row]])

class game:

    def __init__(self):
        self.board = board(3, 3)

    def start(self, cells):
        self.board.initialize_board(cells)
        self.board.print_board()

def main():
    cells = input('Enter cells: > ')
    newgame = game()
    newgame.start(cells)


if __name__ == "__main__":
    main()
