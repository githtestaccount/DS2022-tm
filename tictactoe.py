from sys import exit
from random import choice

# game board indices mapped to numpad numbers
def draw_board(bi):
    print("\n")
    print("     |     |")
    print(f"  {bi[6]}  |  {bi[7]}  |  {bi[8]}")
    print('_____|_____|_____') 
    print("     |     |")
    print(f"  {bi[3]}  |  {bi[4]}  |  {bi[5]}")
    print('_____|_____|_____')
    print("     |     |")
    print(f"  {bi[0]}  |  {bi[1]}  |  {bi[2]}")
    print("     |     |")
    print("\n")
    
def check_continue():
    while True:
        try:
            print("Play on? (0 = no, 1 = yes): ", end="")
            play_on = int(input()) 
        except ValueError:
            print("Ony numbers 0 or 1, please!")
            continue
    
        if play_on < 0 or play_on > 1:
            print("Ony numbers 0 or 1, please!")
            continue
        
        if play_on == 1:
            return True
        else:
            exit()

# check player's row counters for complete rows, colums, diagonals
def check_winner(row_counter, player):
    wins = [[7,8,9], [4,5,6], [1,2,3],
            [7,4,1], [8,5,2], [9,6,3], 
            [7,5,3], [9,5,1]]
 
    for row in wins:
        if all(y in row_counter[player] for y in row):
            return True
    return False    
 
def check_tie(row_counter):
    if len(row_counter['X']) + len(row_counter['O']) == 9:
        return True
    return False

# play one round
def game(player):
    
    # init empty board
    board_indices = [' ' for x in range(9)]
     
    # init player's individual row counters
    row_counter = {'X':[], 'O':[]}
    
    # game loop
    while True:
        draw_board(board_indices)
        # get move input
        try:
            print("Player ", player, " is on the move: ", end="")
            move = int(input()) 
        except ValueError:
            print("Ony numbers 1 to 9, please!")
            continue
        # check boarders
        if move < 1 or move > 9:
            print("Ony numbers 1 to 9, please!")
            continue 
        # check free
        if board_indices[move-1] != ' ':
            print("Choose a free sqaure, please!")
            continue

        # update board 
        board_indices[move-1] = player 
        # update row counter
        row_counter[player].append(move)
        
        # check winner
        if check_winner(row_counter, player):
            draw_board(board_indices)
            print("Player ", player, " wins!")
            return
        # check tie
        if check_tie(row_counter):
            draw_board(board_indices)
            print("No one wins!")
            return
 
        # switch player on the move
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

if __name__ == "__main__":
    
    # print instructions banner once
    print("\n")
    print("Tic Tac Toe console game")
    print("\n")
    print("Instructions:")
    print("Player X and Player Y may use \nthe numpad to make a move")
    draw_board([1,2,3,4,5,6,7,8,9])

    while check_continue():        
        game(choice(["O", "X"]))
    check_continue()