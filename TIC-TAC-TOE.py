# Contributor Name : Rayan Abdul Gafoor

import os

def flag_assignment():
    global player,p,status,board
    player=1
    p=1 # Player Flag [when p==1 player 1's turn, when p==2 player 2's Turn]
    status=-1
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def showboard():
    print(" %c | %c | %c" %(board[0],board[1],board[2]))
    print('___|___|___')
    print(" %c | %c | %c" %(board[3],board[4],board[5]))
    print('___|___|___')
    print(" %c | %c | %c" %(board[6],board[7],board[8]))
    print('   |   |   \n')
    print('Player 1: X')
    print('Player 2: O\n')

def update_board(pos):
    global flag
    global player
    global p
    if player%2==0:
        flag='O'
    else:
        flag='X'
    if board[pos-1]==' ':
        board[pos-1]=flag
        player +=1
        if flag=='X':p=2
        else:p=1
    os.system('cls')
    showboard()


def checkgame():
    global status
    # status == -1 [Running]
    # status == 0  [DRAW]
    # status == 1  [PLAYER 1 WON]
    # status == 2  [PLAYER 2 WON]
    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[6]==board[4]==board[2]=='X':
        status=1 
        print('Player 1 Won')
        gamechoice()
    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[6]==board[4]==board[2]=='O':
        status=2
        print('Player 2 Won')
        gamechoice()
    else:
        if ' ' not in board:
            status=0
            print('Draw')
            gamechoice()

    return status

def gamechoice():
    choice=input('Please enter \'q\' to quit or \'p\' to play again: ')
    if choice=='q':
        quit()
    elif choice=='p':
        flag_assignment()
        os.system('cls')
        showboard()

os.system("cls")
showboard()
while status==-1:
    pos=int(input('Player %d please enter the position (1-9): '%p))
    update_board(pos)
    checkgame()

