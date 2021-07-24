#!/usr/bin/env python3


class Board:

    def __init__(self, size):
        self.board_size = size
        self.filler = self.make_filler()
        self.grid = self.make_board_grid()
        self.cell_dict = dict()
        self.win_condition = self.define_win_condition()

    def __str__(self):
        return self.print_board()

    def is_cell_available(self, cell: int):
        if cell not in self.cell_dict:
            print(f"Sorry, {cell} is not a valid play! Try again.")
            print(self.cell_dict)
            return False
        elif cell in self.cell_dict:
            return True

    def make_board_grid(self):
        board = []
        # Make rows, each row a list
        for i in range(0, self.board_size):
            board.append(i)
            board[i] = []

            # Make cells within each row
            for j in range(0, self.board_size):
                board[i].append(' ')

        return tuple(board)

    def make_filler(self):
        filler = '-'
        for _ in range(0, self.board_size):
            filler += '--------'
        filler += "\n"

        return filler

    def mark_cell(self, index, player_mark):
        row, column = self.cell_dict[index]
        if self.grid[row][column] == ' ':
            self.grid[row][column] = player_mark
            return True
        else:
            print("Sorry... that's taken...")
            return False

    def print_board(self):
        # Reset board output
        board_output = self.filler

        cell_number_label = 0
        for row_index, row in enumerate(self.grid):
            # Placeholder list to store what is in each cell
            row_line_filled_in = []

            for col_index, _ in enumerate(row):  # Yikes from here forward :/
                cell_number_label = int(str(cell_number_label).strip('( )')) + 1

                # Formatting for numbers of different sizes. Extra space on single digits.
                if 1 <= cell_number_label <= 9:
                    cell_number_pretty_label = " (" + str(cell_number_label) + ") "
                else:
                    cell_number_pretty_label = "(" + str(cell_number_label) + ") "

                # If empty, append index to row_line_filled_in, else append what is on cell, X or O.
                if self.grid[row_index][col_index] == ' ':
                    row_line_filled_in.append(str(cell_number_pretty_label))
                else:
                    row_line_filled_in.append(self.grid[row_index][col_index])

                # Add each cell to map with it's coordinates
                self.cell_dict[cell_number_label] = [row_index, col_index]

            # Add the row to board_output
            board_output += "| " + " | ".join(row_line_filled_in) + " |\n"
            board_output += self.filler

        return board_output

    def find_winner(self, index, mark):
        row, column = self.cell_dict[index]
        winner = False

        check_list = [
            self.check_column,
            self.check_row,
            self.check_all_diagonals_1,
            self.check_all_diagonals_2,
        ]

        if self.board_size > 3:
            check_list.extend([
                self.check_all_diagonals_3,
                self.check_all_diagonals_4,
            ])

        for check in check_list:
            tmp_grid = list(self.grid[:])
            winner = check(tmp_grid, mark, row, column)
            if winner:
                break

        if winner:
            print(self)
            print("Congrats! The " + mark.strip() + "'s win!")
            exit()

        if self.check_draw():
            print("It's a draw! Congrats on wasting your time!")
            exit()

    def check_draw(self):
        draw = False
        for row in self.grid:
            for column in row:
                if column == ' ':
                    draw = False
                    return draw
                else:
                    draw = True
        return draw

    def check_column(self, tmp_grid, mark, *coordinates):
        _, column = coordinates
        streak = 0
        condition = False
        for row, _ in enumerate(tmp_grid):
            if streak == self.win_condition:
                return True
            else:
                if tmp_grid[row][column] != mark:
                    streak = 0
                    continue
                elif tmp_grid[row][column] == mark:
                    streak += 1
                    if streak == self.win_condition:
                        return True
                    continue

        return condition

    def check_row(self, tmp_grid, mark, *coordinates):
        row, _ = coordinates
        streak = 0
        condition = False
        for item in tmp_grid[row]:
            if item != mark:
                streak = 0
                continue
            elif item == mark:
                streak += 1
                if streak == self.win_condition:
                    return True
                continue

        return condition

    def check_all_diagonals_1(self, tmp_grid, mark, *coordinates):
        """
            This is a sample 4x4 with a win condition of 3.
            It starts at the cell equal to the win condition within it's row.
            It checks the down-left diagonal from that cell.
            It then moves until the corner within that row (>) doing the same.
                                v   # Starting here, on 3, then moving right (>).
            ---------------------------------
            |  (1)  |  (2)  |   X   |   X   |
            ---------------------------------
            |  (5)  |   X   |   X   |  (8)  |
            ---------------------------------
            |   X   |   X   | (11)  | (12)  |
            ---------------------------------
            |   X   | (14)  | (15)  | (16)  |
            ---------------------------------
        """
        streak = 0
        condition = False
        # We aren't using last play for this condition check. Brute Forcing FTW
        column = self.win_condition - 1  # First diagonal is win condition, starting at 0
        rev_column = column
        while column < self.board_size and rev_column >= 0:
            for row in tmp_grid:
                if rev_column < 0:
                    break
                if row[rev_column] != mark:
                    streak = 0
                    rev_column -= 1
                    continue
                elif row[rev_column] == mark:
                    streak += 1
                    if streak == self.win_condition:
                        return True
                    rev_column -= 1
                    continue
            rev_column = column
            column += 1

        return condition

    def check_all_diagonals_2(self, tmp_grid, mark, *coordinates):
        """
            This is a sample 4x4 with a win condition of 3.
            It starts at the cell equal to the win condition within it's row.
            It checks the up-left diagonal from that cell.
            It then moves until the corner within that row (>) doing the same.
            ---------------------------------
            |   X   |  (2)  |  (3)  |  (4)  |
            ---------------------------------
            |   X   |   X   |  (7)  |  (8)  |
            ---------------------------------
            |  (9)  |   X   |   X   | (12)  |
            ---------------------------------
            | (13)  | (14)  |   X   |   X   |
            ---------------------------------
                                ^   # Starting here, on 15, then moving right (>).
        """
        tmp_grid.reverse()
        condition = self.check_all_diagonals_1(tmp_grid, mark, coordinates)

        return condition

    def check_all_diagonals_3(self, tmp_grid, mark, *coordinates):
        """
            This is a sample 4x4 with a win condition of 3.
            It starts at the cell equal to the win condition within it's row.
            It checks the down-right diagonal from that cell.
            It then moves until the corner within that row (<) doing the same.
                        v   # Starting here, on 2, then moving left (<).
            ---------------------------------
            |   X   |   X   |  (3)  |  (4)  |
            ---------------------------------
            |  (5)  |   X   |   X   |  (8)  |
            ---------------------------------
            |  (9)  | (10)  |   X   |   X   |
            ---------------------------------
            | (13)  | (14)  | (15)  |   X   |
            ---------------------------------
        """
        for row in tmp_grid:
            row.reverse()
        condition = self.check_all_diagonals_1(tmp_grid, mark, coordinates)

        return condition

    def check_all_diagonals_4(self, tmp_grid, mark, *coordinates):
        """
            This is a sample 4x4 with a win condition of 3.
            It starts at the cell equal to the win condition within it's row.
            It checks the up-right diagonal from that cell.
            It then moves until the corner within that row (<) doing the same.
            ---------------------------------
            |  (1)  |  (2)  |  (3)  |   X   |
            ---------------------------------
            |  (5)  |  (6)  |   X   |   X   |
            ---------------------------------
            |  (9)  |   X   |   X   | (12)  |
            ---------------------------------
            |   X   |   X   | (15)  | (16)  |
            ---------------------------------
                        ^   # Starting here, on 14, then moving left (<).
        """
        for row in tmp_grid:
            row.reverse()
        tmp_grid.reverse()
        condition = self.check_all_diagonals_1(tmp_grid, mark, coordinates)

        return condition

    def define_win_condition(self):
        if self.board_size % 2 == 0 and self.board_size > 4:
            return int(self.board_size / 2)
        elif self.board_size % 2 == 1 and self.board_size > 5:
            return int(self.board_size / 2) + 1
        else:
            return 3


if __name__ == "__main__":
    the_board = Board(3)
    the_board.print_board()
