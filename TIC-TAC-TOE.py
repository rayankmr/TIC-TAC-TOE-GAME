# Contributor Name : Rayan Abdul Gafoor

import os
game_count=1
player_name=[]
player_name2=[]

def flag_assignment():
    global player,p,status,board
    player=1
    p=player_name2[0] 
    status=-1
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def showboard():
    global game_count
    print('|  GAME %d |' %game_count)
    print('-----------')
    print(" %c | %c | %c" %(board[0],board[1],board[2]))
    print('___|___|___')
    print(" %c | %c | %c" %(board[3],board[4],board[5]))
    print('___|___|___')
    print(" %c | %c | %c" %(board[6],board[7],board[8]))
    print('   |   |   \n')
    print('Player [ %s ]: X' %player_name2[0])
    print('Player [ %s ]: O\n' %player_name2[1])

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
        if flag=='X':p=player_name2[1]
        else:p=player_name2[0]
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
        print('%s Won this game' %player_name2[0])
        score[player_name2[0]]=score[player_name2[0]] +1
        gamechoice()
    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[6]==board[4]==board[2]=='O':
        status=2
        print('%s Won this game' %player_name2[1])
        score[player_name2[1]]=score[player_name2[1]] +1
        gamechoice()
    else:
        if ' ' not in board:
            status=0
            print('Draw')
            gamechoice()

    return status

def gamechoice():
    global game_number
    global game_count
    if game_number==1:
        # quit()
        if input('Please enter \'s\' to show the final score: ') =='s':
            print_score()
        
    else:
        choice=input('Please enter \'q\' to quit or \'c\' to continue: ')
        if choice=='q':
            # quit()
            print_score()
        elif choice=='c':
            game_number= game_number-1
            game_count= game_count+1
            player_name2.reverse()
            flag_assignment()
            os.system('cls')
            showboard()
            
def print_score():
    os.system('cls')
    print('---------------') 
    print('     SCORE    ')  
    print('---------------')
    print(' %s : %d' %(player_name[0],score[player_name[0]]))
    print('---------------')
    print(' %s : %d\n' %(player_name[1],score[player_name[1]]))


os.system("cls")
game_number=int(input('Please enter the number of game:'))

for i in range(2):
    player_name.append((input('Plese enter name of player %d: ' %(i+1))).capitalize())
for i in range(2):
    player_name2.append(player_name[i])
score={player_name[0]:0,player_name[1]:0}

os.system("cls")
flag_assignment()
showboard()
while status==-1:
    pos=int(input('%s please enter the position (1-9): '%p))
    update_board(pos)
    checkgame()

