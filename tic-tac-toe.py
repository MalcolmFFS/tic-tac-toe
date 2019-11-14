#!/usr/bin/env python3

"""
TODO:
dirty rows/columns (victory cannot be achieved, end game early)
    Going to need to do this once per victory condition
    Most likely easiest to base off of victory condition function.
    Not super easy...
    Have to make sure it doesn't exit if one victory condition can't be met
    but other still can...
    I think if a victory condition can't be met, I remove it from conditions[]
    And if that's empty, I say "no winning condition remains"
"""

import re

def get_board_size():
    while True:
        size_raw = input("What size board do you want (3-9)?\n-$ ")
        try:
            size_int = int(size_raw)
            if size_int > 2 and size_int < 10:
                return size_int
            else:
                print("Sorry, you entered a size we can't accept. Try again...")
                continue
        except ValueError:
            print("Sorry, you didn't enter an int. Try again...")
            continue


def make_filler():
    filler = '-'
    for _ in range(0, size):
        filler += '--------'

    return filler


def gen_board():
    filler = make_filler()
    board_out = filler + "\n"
    line_filled = []
    cell_number = 0
    for r_index,row in enumerate(board):
        for c_index,_ in enumerate(row): # Yikes from here forward :/
            try:
                cell_number = cell_number + 1
            except TypeError:
                cell_number = int(cell_number.strip('( )')) + 1
            if cell_number >= 1 and cell_number <= 9:
                cell_number = " (" + str(cell_number) + ") "
            else:
                cell_number = "(" + str(cell_number) + ") "

            if board[r_index][c_index] == ' ':
                line_filled.append(str(cell_number))
            else:
                line_filled.append(board[r_index][c_index])
            cell_dict[str(cell_number).strip('( )')] = [r_index, c_index]

        board_out += "| " + " | ".join(line_filled) + " |\n"
        board_out += filler + "\n"
        line_filled = []

    return board_out


def make_board_array():
    board = []
    for i in range(0, size):
        board.append(i)
        board[i] = []

        for j in range(0, size):
            board[i].append(' ')

    return board


def make_play(player: str,):
    if player == 1:
        player_mark = '  O  '
        player_name = 'Player 1'
    elif player == 2:
        player_mark = '  X  '
        player_name = 'Player 2'
    while True:
        coords = validate_coordinates(player_name)
        if board[coords[0]][coords[1]] == ' ':
            board[coords[0]][coords[1]] = player_mark
        else:
            print("Sorry... that's taken...")
            continue
        break

    find_winner(coords,player_mark)

    return board


def validate_coordinates(player_name):
    while True:
        play = input(player_name + ", enter your cell: ")
        play = play.strip('()')
        if play not in cell_dict:
            print("Sorry, that's not a valid play! Try again.")
            continue
        elif play in cell_dict:
            coords = cell_dict[play]
            return coords


def find_winner(coords,player_mark):
    row, column = coords
    mark = player_mark
    win_condition = False
    conditions=[
        check_column,
        check_row,
        check_diagonal,
        check_diagonal_up,
        ]

    for condition in conditions:
        win_condition = condition(board[:], row, column, mark)
        if win_condition:
            print(gen_board())
            print("Congrats! The " + mark.strip() + "'s win!")
            exit()

    if check_draw():
        print("It's a draw! Congrats on wasting your time!")
        exit()


def check_draw():
    draw = False
    for line in board:
        for item in line:
            if item == ' ':
                draw = False
                return draw
            else: draw = True
    return draw


def check_column(tmp_board, row, column, i):
    streak = 0
    condition = False
    for index,_ in enumerate(tmp_board):
        if streak == win_condition:
            return True
        else:
            if tmp_board[index][column] != i:
                streak = 0
                continue
            elif tmp_board[index][column] == i:
                streak += 1
                if streak == win_condition:
                    return True
                continue

    return condition


def check_row(tmp_board, row, column, i):
    streak = 0
    condition = False
    for item in tmp_board[row]:
        if item != i:
            streak = 0
            continue
        elif item == i:
            streak += 1
            if streak == win_condition:
                return True
            continue

    return condition


def check_diagonal(tmp_board,row,column,i):
    streak = 0
    condition = False
    for index,_ in enumerate(tmp_board):
        if tmp_board[index][index] != i:
            streak = 0
            continue
        elif tmp_board[index][index] == i:
            streak += 1
            if streak == win_condition:
                return True
        else:
            streak = 0
            continue

    return condition


def check_diagonal_up(tmp_board,x,y,i):
    tmp_board.reverse()
    condition = check_diagonal(tmp_board,x,y,i)

    return condition


def define_win_condition(size):
    if size % 2 == 0 and size > 4:
        return int(size / 2)
    elif size % 2 == 1 and size > 5:
        return int(size / 2) + 1
    else:
        return 3

if __name__ == "__main__":
    global win_condition
    global cell_dict
    global size
    global board
    cell_dict = {}
    p1 = 1
    p2 = 2
    size = get_board_size()
    win_condition = define_win_condition(size)
    board = make_board_array()
    print(gen_board())

    while True:
        make_play(p1)
        print(gen_board())
        make_play(p2)
        print(gen_board())
        continue
