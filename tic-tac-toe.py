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
        size = input("What size board do you want (3-101)?\n-$ ")
        try:
            size_int = int(size)
            if size_int > 2 and size_int < 102:
                return size_int
            else:
                print("Sorry, you entered a size we can't accept. Try again...")
                continue
        except ValueError:
            print("Sorry, you didn't enter an int. Try again...")
            continue


def make_board_header(size):
    board_out = "   | "
    for i in range(1, size + 1):
        board_out += str(i) + " | "

    board_out = board_out.rstrip()
    board_out += "\n"

    return board_out


def make_filler(header):
    filler = ''
    for _ in range(0,len(header)):
        filler += '-'

    return filler


def gen_board(size,board):
    board_out = make_board_header(size)
    filler = make_filler(board_out)
    line_filled = ""
    for index,line in enumerate(board, start=1):
        for item in line:
            line_filled += item
        board_out += " " + str(index) + " | " + " | ".join(line_filled) + " |\n"
        board_out += filler + "\n"
        line_filled = ""

    return board_out


def make_board_array(size: int):
    board = []
    for i in range(1, size + 1):
        board.append(i)
        board[i - 1] = []

        for j in range(1, size + 1):
            board[i - 1].append(' ')

    return board


def make_play(player: str,board, size):
    if player == 1:
        player_mark = 'O'
        player_name = 'Player 1'
    elif player == 2:
        player_mark = 'X'
        player_name = 'Player 2'
    while True:
        coords = validate_coordinates(size,player_name)
        if board[coords[1] - 1][coords[0] - 1] == ' ':
            board[coords[1] - 1][coords[0] - 1] = player_mark
        else:
            print("Sorry... that's taken...")
            continue
        break

    find_winner(board,coords,player_mark)

    return board


def validate_coordinates(size,player_name):
    while True:
        valid = False
        play = input(player_name + ", enter your coordinates (column,row): ")
        if re.match(r'\d*\.\d+', play):
            print("Sorry, we don't accept float numbers here... Try again!")
            continue
        elif re.match(r'^\d+,\d+$', play):
            coords = play.split(',')
            coords = [int(i) for i in coords]
            for i in coords:
                if i > 0 and i <= size:
                    valid = True
                else:
                    valid = False
                    print("Sorry, your coordinates are out of range...")
                    break
            if valid:
                return coords
            continue
        else:
            print("Sorry, you didn't enter valid coordinates...")
            continue


def find_winner(board,coords,player_mark):
    x, y = coords
    x, y = x - 1, y - 1
    i = player_mark
    win_condition = False
    conditions=[
        check_vertical,
        check_horizontal,
        check_diagonal,
        check_diagonal_up,
        ]

    for condition in conditions:
        win_condition = condition(board[:],x,y,i)
        if win_condition:
            print("Congrats! The " + i + "'s win!")
            exit()

    if check_draw(board):
        print("It's a draw! Congrats on wasting your time!")
        exit()


def check_draw(board):
    draw = False
    for line in board:
        for item in line:
            if item == ' ':
                draw = False
                return draw
            else: draw = True
    return draw


def check_vertical(board,x,y,i):
    streak = 0
    condition = False
    for index,_ in enumerate(board):
        if streak == win_condition:
            return True
        else:
            if board[index][x] != i:
                streak = 0
                continue
            elif board[index][x] == i:
                streak += 1
            else:
                streak = 0
                continue

    return condition


def check_horizontal(board,x,y,i):
    streak = 0
    condition = False
    for item in board[y]:
        if streak == win_condition:
            return True
        else:
            if item != i:
                streak = 0
                continue
            elif item == i:
                streak += 1
            else:
                streak = 0
                continue

    return condition


def check_diagonal(board,x,y,i):
    streak = 0
    condition = False
    for index,_ in enumerate(board):
        if streak == win_condition:
            return True
        else:
            if board[index][index] != i:
                streak = 0
                continue
            elif board[index][index] == i:
                streak += 1
            else:
                streak = 0
                continue

    return condition


def check_diagonal_up(board,x,y,i):
    board.reverse()
    condition = check_diagonal(board,x,y,i)

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
    p1 = 1
    p2 = 2
    size = get_board_size()
    win_condition = define_win_condition(size)
    board = make_board_array(size)
    print(gen_board(size,board))

    while True:
        make_play(p1,board,size)
        print(gen_board(size, board))
        make_play(p2, board,size)
        print(gen_board(size, board))
        continue