class board:
    _width = 0
    _height = 0
    _x_count = 0
    _circle_count = 0
    _cells = []
    _empty_cell = '_'
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
    
    def has_empty_cells(self):
        spaces = 0
        for row in range(0, len(self._cells)):
            spaces += self._cells[row].count(self._empty_cell)
        return True if spaces > 0 else False
    
    def who_win(self, character):
        for number in range(0, self._width):
            row_win = self._cells[number].count(character) == 3
            col_win = [self._cells[0][number],self._cells[1][number],self._cells[2][number]].count(character) == 3
            if col_win or row_win:
                return col_win or row_win
        if [self._cells[0][0],self._cells[1][1],self._cells[2][2]].count(character) == 3:
            return True
        if [self._cells[0][2],self._cells[1][1],self._cells[2][0]].count(character) == 3:
            return True
        return False
    

class game:
    _states = {1: 'Game not finished', 2: 'Draw', 3: 'X wins', 4: 'O wins', 5: 'Impossible'}
    
    def __init__(self):
        self.board = board(3, 3)
        self.state = self._states[1]

    def start(self, cells):
        self.board.initialize_board(cells)
        self.board.print_board()
        self.set_state()
        print(self.state)

    def count_cells(self, character):
        count = 0
        for item in self.board._cells:
            count += item.count(character)
        return count
    def set_state(self):
        x_win = self.board.who_win('X')
        o_win = self.board.who_win('O')
        x_count = self.count_cells('X')
        o_count = self.count_cells('O')
        if not x_win and not o_win and self.board.has_empty_cells():
            self.state = self._states[1]
        if not x_win and not o_win and not self.board.has_empty_cells():
            self.state = self._states[2]
        if x_win and not o_win:
            self.state = self._states[3]
        if o_win and not x_win:
            self.state = self._states[4]
        if o_win and x_win or (x_count - o_count > 1) or (o_count - x_count > 1):
            self.state = self._states[5]


def main():
    cells = input('Enter cells: > ')
    newgame = game()
    newgame.start(cells)


if __name__ == "__main__":
    main()
