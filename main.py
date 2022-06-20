from random import randint
from time import sleep
import os

board = [' ' for x in range(10)]

def print_board():
    spaces = " " * 75
    print('\n'*2)
    print(f'{spaces}   |   |')
    print(f'{spaces} {board[1]} | {board[2]} | {board[3]} ')
    print(f'{spaces}   |   |')
    print(f'{spaces}-----------')
    print(f'{spaces}   |   |')
    print(f'{spaces} {board[4]} | {board[5]} | {board[6]} ')
    print(f'{spaces}   |   |')
    print(f'{spaces}-----------')
    print(f'{spaces}   |   |')
    print(f'{spaces} {board[7]} | {board[8]} | {board[9]} ')
    print(f'{spaces}   |   |')
    print('\n'*2)

def is_filled(pos):
    return board[pos] != ' '

def is_win(board, letter):
    return board[1] == board[2] == board[3] == letter or\
           board[4] == board[5] == board[6] == letter or\
           board[7] == board[8] == board[9] == letter or\
           board[1] == board[4] == board[7] == letter or\
           board[3] == board[6] == board[9] == letter or\
           board[2] == board[5] == board[8] == letter or\
           board[1] == board[5] == board[9] == letter or\
           board[3] == board[5] == board[7] == letter

def is_draw():
    return ' ' not in board[1:]

def calculate_move():
    print('Calculating Next Move...')
    sleep(2)

def player_move():
    if_end_game()
    while True:
        try:
            pos = int(input('Please select a position to place a "X" (1-9): '))
            
            if not is_filled(pos):
                board[pos] = 'X'
                break
            else:
                print_board()
                print('This place is already filled. Try again')
        except:
            quit()

def pc_move():
    if_end_game()
    calculate_move()
    if os.uname().sysname == 'Linux':
        os.system('clear')

    # Strategy 1
    # Win
    for pos, field in enumerate(board):
        copy_board = board[:]
        if field == ' ':
            copy_board[pos] = 'O'
            if is_win(copy_board, 'O'):
                board[pos] = 'O'
                return

    # Strategy 2
    # Prevent player from winning
    for pos, field in enumerate(board):
        copy_board = board[:]
        if field == ' ':
            copy_board[pos] = 'X'
            if is_win(copy_board, 'X'):
                board[pos] = 'O'
                return

    # Strategy 3
    # Fill Middle
    if not is_filled(5):
        board[5] = 'O'
        return

    # Strategy 4
    # Fill Corners
    for pos, field in enumerate(board):
        open_corners = tuple(filter(lambda x: not is_filled(x), (1, 3, 7, 9)))
        copy_board = board[:]
        if len(open_corners) > 0:
            board[open_corners[randint(0, len(open_corners))-1]] = 'O'
            return

    # Strategy 5
    # Fill Sides
    for pos, field in enumerate(board):
        open_sides = tuple(filter(lambda x: not is_filled(x), (2, 4, 6, 8)))
        copy_board = board[:]
        if len(open_sides) > 0:
            board[open_sides[randint(0, len(open_sides))-1]] = 'O'
            return


def clear_board():
    for c in range(1, 10):
        board[c] = ' '

def keep():
    keep = int(input('Continue? [1-Yes|2-No]: '))
    while keep != 1 and keep != 2:
        print('Invalid Value\n')
        keep = int(input('Continue? [1-Yes|2-No]: '))
    if keep == 1:
        clear_board()
        return
    quit()

def if_end_game():
    if is_win(board, 'X'):
        print('You Win!!!')
        keep()

    elif is_win(board, 'O'):
        print('You Lose')
        keep()

    elif is_draw():
        print('Draw')
        keep()

def run():
    while True:
        print_board()
        player_move()
        print_board()        
        pc_move()


run()





