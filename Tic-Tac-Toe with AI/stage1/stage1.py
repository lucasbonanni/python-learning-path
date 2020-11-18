class Board:
    width = 0
    _height = 0
    _x_count = 0
    _circle_count = 0
    cells = []
    _empty_cell = ' '

    def __init__(self, width, height):
        self.width = width
        self._height = height

    @staticmethod
    def print_frame_line():
        print('---------')

    @staticmethod
    def print_row(line):
        print('| ' + ' '.join(line) + ' |')

    def print_board(self):
        Board.print_frame_line()
        for col in range(self.width - 1, -1, -1):
            Board.print_row([self.cells[0][col], self.cells[1]
            [col], self.cells[2][col]])
        Board.print_frame_line()

    def initialize_board(self, cells):
        cells = cells.replace('_', ' ')
        for row in range(0, self.width):
            self.cells.append(
                [cells[6 + row], cells[3 + row], cells[0 + row]])

    def has_empty_cells(self):
        spaces = 0
        for row in range(0, len(self.cells)):
            spaces += self.cells[row].count(self._empty_cell)
        return True if spaces > 0 else False

    def who_win(self, character):
        for number in range(0, self.width):
            row_win = self.cells[number].count(character) == 3
            col_win = [self.cells[0][number], self.cells[1]
            [number], self.cells[2][number]].count(character) == 3
            if col_win or row_win:
                return col_win or row_win
        if [self.cells[0][0], self.cells[1][1], self.cells[2][2]].count(character) == 3:
            return True
        if [self.cells[0][2], self.cells[1][1], self.cells[2][0]].count(character) == 3:
            return True
        return False

    def is_in_range(self, x):
        return x < self.width

    def cell_is_occupied(self, x, y):
        return False if self.cells[x][y] == self._empty_cell else True


class Game:
    _states = {1: 'Game not finished', 2: 'Draw', 3: 'X wins', 4: 'O wins', 5: 'Impossible'}

    def __init__(self):
        self.board = Board(3, 3)
        self.state = 1

    def start(self, cells):
        self.board.initialize_board(cells)
        self.board.print_board()
        while self.state == 1:
            coordenates = self.read_coordenates()
            self.make_a_move(coordenates)
            self.board.print_board()
            self.set_state()
            break # on the stage 1 just need to run one time
        print(self._states[self.state])

    def countcells(self, character):
        count = 0
        for item in self.board.cells:
            count += item.count(character)
        return count

    def set_state(self):
        x_win = self.board.who_win('X')
        o_win = self.board.who_win('O')
        x_count = self.countcells('X')
        o_count = self.countcells('O')
        if not x_win and not o_win and self.board.has_empty_cells():
            self.state = 1
        if not x_win and not o_win and not self.board.has_empty_cells():
            self.state = 2
        if x_win and not o_win:
            self.state = 3
        if o_win and not x_win:
            self.state = 4
        if o_win and x_win or (x_count - o_count > 1) or (o_count - x_count > 1):
            self.state = 5

    def read_coordenates(self):
        is_valid = False
        res = []
        resp = ''
        is_in_range = False
        is_available = False
        is_numeric = False
        x = 0
        y = 0
        while not is_valid:
            try:
                resp = input('Enter the coordinates: ')
            except:
                pass
            if len(resp) > 0 and not resp.isspace():
                res = resp.split()
                is_numeric = (res[0].isnumeric() and res[1].isnumeric())
                if not is_numeric:
                    print('You should enter numbers!')
                if is_numeric:
                    x = int(res[0]) - 1
                    y = int(res[1]) - 1
                    is_in_range = (self.board.is_in_range(x) and self.board.is_in_range(y))
                    if not is_in_range:
                        print(f'Coordinates should be from {1} to {self.board.width}!')
                    elif is_in_range:
                        is_available = not self.board.cell_is_occupied(x, y)
                        if not is_available and is_in_range:
                            print('This cell is occupied! Choose another one!')
            is_valid = is_numeric and is_in_range and is_available
        return [x, y]

    def feel_cell(self, x, y, character):
        self.board.cells[x][y] = character

    def make_a_move(self, coordenates):
        count_x = self.countcells('X')
        count_o = self.countcells('O')
        if count_o == count_x:
            self.feel_cell(coordenates[0], coordenates[1], 'X')
        elif count_x - count_o == 1:
            self.feel_cell(coordenates[0], coordenates[1], 'O')


def main():
    cells = input('Enter cells: ')
    # cells = '_________'
    newgame = Game()
    newgame.start(cells)


if __name__ == "__main__":
    main()
