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

    def has_empty_cells(self):
        spaces = 0
        for row in range(0, len(self._cells)):
            spaces += self._cells[row].count(' ')
        return True if spaces > 0 else False

    def cell_is_occupied(self, x, y):
        return False if self._cells[x][y] == ' ' else True

    def initialize_board(self, cells):
        cells = cells.replace('_', ' ')
        for row in range(0, self._width):
            self._cells.append(
                [cells[6 + row], cells[3 + row], cells[0 + row]])

    def is_in_range(self, x):
        return x < self._width


class game:
    _states = {1: 'Game not finished', 2: 'Draw', 3: 'X wins', 4: 'O wins'}

    def __init__(self):
        self.board = board(3, 3)
        self.state = self._states[1]

    def read_coordenates(self):
        is_valid = False
        res = ''
        while not is_valid:
            res = input('Enter the coordinates: > ').split()
            is_numeric = (res[0].isnumeric() and res[1].isnumeric())
            if not is_numeric:
                print('You should enter numbers!')
            if is_numeric:
                x = int(res[0]) - 1
                y = int(res[1]) - 1
                is_in_range = (self.board.is_in_range(
                    x) and self.board.is_in_range(y))
                if not is_in_range:
                    print(
                        f'Coordinates should be from {1} to {self.board._width}!')
                elif is_in_range:
                    is_available = not self.board.cell_is_occupied(x, y)
                    if not is_available and is_in_range:
                        print('This cell is occupied! Choose another one!')
            is_valid = is_numeric and is_in_range and is_available
        return [x, y]

    def count_cells(self, character):
        count = 0
        for item in self.board._cells:
            count += item.count(character)
        return count

    def feel_cell(self, x, y, character):
        self.board._cells[x][y] = character

    def make_a_move(self, coordenates):
        count_x = self.count_cells('X')
        count_o = self.count_cells('O')
        if(count_o > count_x):
            self.feel_cell(coordenates[0], coordenates[1], 'O')
        else:
            self.feel_cell(coordenates[0], coordenates[1], 'X')

    def start(self, cells):
        self.board.initialize_board(cells)
        self.board.print_board()
        coordenates = self.read_coordenates()
        self.make_a_move(coordenates)


def main():
    cells = input('Enter cells: > ')
    newgame = game()
    newgame.start(cells)


if __name__ == "__main__":
    main()
