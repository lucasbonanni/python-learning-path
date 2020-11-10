class cell:
    def init(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
    
    def is_ocupied(self):
        return cell.is_filled(self.char)

    @staticmethod
    def validate_char(char):
        return cell.is_filled(char) or char == '_'
    
    @staticmethod
    def is_filled(char):
        return char == 'X' or char == 'O'

class board:
    _width = 0
    _height = 0
    def __init__(self,width, height, cells):
        self._width = width
        self._height = height
        self.print_board(cells)

    def print_frame_line(self):
        print('---------')

    def print_row(self, line):
        print('| ' + ' '.join(line) + ' |')

    def print_board(self, cells):
        cells = cells.replace('_',' ')

        rows = [cells[0:3],cells[3:6],cells[6:9]]
        self.print_frame_line()
        for row in rows:
            self.print_row(row)
        self.print_frame_line()

class game:
    def __init__(self, cells):
        self.board = board(3,3,cells)


def main():
    cells = input('Enter cells: > ')
    game(cells)




if __name__ == "__main__":
    main()