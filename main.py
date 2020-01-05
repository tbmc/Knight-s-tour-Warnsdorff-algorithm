class WarnsdorffAlgorithm:

    board = [[]]
    move_counter = 0
    __moves = (
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),

        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2),
    )

    def __init__(self, number_cells=8):
        self.board = [[None] * number_cells for i in range(number_cells)]

    def __is_cell_available(self, line: int, col: int):
        number_cells = len(self.board)
        return 0 <= line < number_cells and 0 <= col < number_cells and self.board[line][col] is None

    def __get_accessible_cells(self, line: int, col: int):
        cells = []
        for line_add, col_add in self.__moves:
            ll = line + line_add
            cc = col + col_add
            if self.__is_cell_available(ll, cc):
                cells.append((ll, cc))
        return cells

    def __get_less_accessible_cell(self, line: int, col: int):
        cell_accessibilities = []
        for line_add, col_add in self.__moves:
            ll = line + line_add
            cc = col + col_add
            if not self.__is_cell_available(ll, cc):
                continue
            cells = self.__get_accessible_cells(ll, cc)
            length = len(cells)
            if length < 1:
                continue
            cell_accessibilities.append((length, (ll, cc)))
        if len(cell_accessibilities) < 1:
            return None
        _, coordinates = min(cell_accessibilities)
        return coordinates

    def __resolve_recursive(self, line, col):
        less_accessible_cell = self.__get_less_accessible_cell(line, col)
        if less_accessible_cell is None:
            return
        line, col = less_accessible_cell
        if not self.__is_cell_available(line, col):
            return
        self.board[line][col] = self.move_counter
        self.move_counter += 1

        self.__resolve_recursive(line, col)

    def resolve(self, start_line=0, start_column=0):
        if not self.__is_cell_available(start_line, start_column):
            return
        self.board[start_line][start_column] = self.move_counter
        self.move_counter += 1
        self.__resolve_recursive(start_line, start_column)

    def print(self):
        for line in self.board:
            cells = []
            for cell in line:
                if cell is None:
                    cells.append("None")
                else:
                    cells.append(f"{cell:>4}")
            print(" ".join(cells))


if __name__ == "__main__":
    warn = WarnsdorffAlgorithm()
    warn.resolve(0, 4)
    warn.print()
