#!/usr/bin/env python3

from board import Board


class Player:

    def __init__(self, player):
        if player == 1:
            self.player_mark = '  O  '
            self.player_name = 'Player 1'
        elif player == 2:
            self.player_mark = '  X  '
            self.player_name = 'Player 2'


def get_board_size():
    while True:
        size_raw = input("What size board do you want (3-9)?\n-$ ")
        try:
            size_int = int(size_raw)
            if 2 < size_int < 10:
                return size_int
            else:
                print("Sorry, you entered a size we can't accept. Try again...")
                continue
        except ValueError:
            print("Sorry, you didn't enter an int. Try again...")
            continue


def make_play():
    while True:
        try:
            return int(input().strip('( )'))
        except ValueError:
            print("Sorry, you didn't enter an int. Try again...")
            continue


def verify_play(player):
    while True:
        print(f"{player.player_name}, enter your cell: ")
        play = make_play()
        available = the_game.is_cell_available(play)
        if not available:
            continue
        elif available:
            if not the_game.mark_cell(play, player.player_mark):
                continue
            the_game.find_winner(play, player.player_mark)
            break


if __name__ == "__main__":
    size = get_board_size()
    the_game = Board(size)
    p1 = Player(1)
    p2 = Player(2)
    print(the_game)

    while True:
        verify_play(p1)
        print(the_game)
        verify_play(p2)
        print(the_game)
        continue
