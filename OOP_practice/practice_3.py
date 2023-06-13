MARK_X = "X"
MARK_O = "O"
MARK_UNKNOWN = ' '


class Cell:
    def __init__(self):
        self.mark = MARK_UNKNOWN

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark


class Board:
    def __init__(self, r=3, c=3):
        self.cells = []
        self.rows = r
        self.columns = c
        for i in range(r * c):
            self.cells.append(Cell())

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def is_available(self, index):
        return self.cells[index - 1].get_mark() == MARK_UNKNOWN

    def get_mark(self, index):
        return self.cells[index - 1].get_mark()

    def set_cell(self, index, mark):
        self.cells[index - 1].set_mark(mark)

    def get_cell(self):
        return self.cells


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark


def win_condition(board):
    win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                 (1, 4, 7), (2, 5, 8), (3, 6, 9),
                 (1, 5, 9), (3, 5, 7)]
    win_mark = MARK_UNKNOWN
    for combo in win_combo:  # в переменную combo передаем кортеж из списка
        m1 = board.get_mark(combo[0])  # -
        m2 = board.get_mark(combo[1])  # раздаем переменным каждый элемент кортежа
        m3 = board.get_mark(combo[2])  # -
        if m1 == m2 == m3:
            win_mark = m1
            break
    return win_mark


def render(board):
    rc = board.get_rows()
    cl = board.get_columns()

    for i in range(rc):
        row = []
        for j in range(cl):
            row.append(board.get_mark(i * cl + j + 1))
        print("|".join(row))


if __name__ == '__main__':
    board = Board()
    board.set_cell(1, MARK_X)
    board.set_cell(4, MARK_X)
    board.set_cell(7, MARK_X)
    # print(win_condition(board))
    render(board)
