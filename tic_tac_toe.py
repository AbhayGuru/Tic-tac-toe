def playboard(player1state,player2state):                   #create a playboard to play tic tac toe game.
    zero= '\033[1m'+'X'+'\033[0m' if player1state[0] else ('\033[1m'+'O'+'\033[0m' if player2state[0] else 0)
    one= '\033[1m'+'X'+'\033[0m' if player1state[1] else ('\033[1m'+'O'+'\033[0m' if player2state[1] else 1)
    two= '\033[1m'+'X'+'\033[0m' if player1state[2] else ('\033[1m'+'O'+'\033[0m' if player2state[2] else 2)
    three= '\033[1m'+'X'+'\033[0m' if player1state[3] else ('\033[1m'+'O'+'\033[0m' if player2state[3] else 3)
    four= '\033[1m'+'X'+'\033[0m' if player1state[4] else ('\033[1m'+'O'+'\033[0m' if player2state[4] else 4)
    five= '\033[1m'+'X'+'\033[0m' if player1state[5] else ('\033[1m'+'O'+'\033[0m' if player2state[5] else 5)
    six= '\033[1m'+'X'+'\033[0m' if player1state[6] else ('\033[1m'+'O'+'\033[0m' if player2state[6] else 6)
    seven= '\033[1m'+'X'+'\033[0m' if player1state[7] else ('\033[1m'+'O'+'\033[0m' if player2state[7] else 7)
    eight= '\033[1m'+'X'+'\033[0m' if player1state[8] else ('\033[1m'+'O'+'\033[0m' if player2state[8] else 8)
    print(' ')
    print(f'\t*-----------*')
    print(f"\t| {zero} | {one} | {two} |")
    print(f"\t|---|---|---|")
    print(f"\t| {three} | {four} | {five} |")
    print(f"\t|---|---|---|")
    print(f"\t| {six} | {seven} | {eight} |")
    print(f"\t*-----------*")

def playerinfo(player1,player2):                            #Store the information of Players by taking the input from user.
    print(' ')
    print('\033[1m Player 1:-',player1.capitalize(),'|| Player 2:-',player2.capitalize()+'\033[0m')
    print(' ')
    print('\t\033[1m'+player1.capitalize()+'\033[0m',"use \033[1m 'X' \033[0m in Game.")
    print('\t\033[1m'+player2.capitalize()+'\033[0m',"use \033[1m 'O' \033[0m in Game.")

def sum(a,b,c):
    return a+b+c

def checkwin(player1state,player2state,player1,player2,count):                  #condition to check the winner.
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(player1state[win[0]], player1state[win[1]], player1state[win[2]])==3):
            print('\033[1m\nWINNER: ',player1.capitalize(),'\033[0m')
            return 1
        
        if(sum(player2state[win[0]], player2state[win[1]], player2state[win[2]])==3):
            print('\033[1m\nWINNER: ',player2.capitalize(),'\033[0m')
            return 0
    return -1

    
    #Main function of the game....

print('*** WELCOME TO TIC TAC TOE GAME ***')

player1state=[0,0,0,0,0,0,0,0,0]             #created the list to save the input of players in game.
player2state=[0,0,0,0,0,0,0,0,0]
turn=1                                       # 1 for X and 0 for O.
playboard(player1state,player2state)         # function calling.
print(' ')
player1=input('ENTER THE PLAYER 1 NAME: ')
player2=input('ENTER THE PLAYER 2 NAME: ')
playerinfo(player1,player2)                  # function calling.

count=0                                      #to count the step moved by the player.
while True:                                  #True means loop forever.
    playboard(player1state, player2state)    #function calling.
    
    if(turn==1):
        print('\n\033[1m',player1.upper(),'CHANCE:-\033[0m')
        value=int(input('Enter The Place: '))
        player1state[value]=1
        count+=1
    else:
        print('\n\033[1m',player2.upper(),'CHANCE:-\033[0m')
        value=int(input('Enter The Place: '))
        player2state[value]=1
        count+=1
        
    cwin= checkwin(player1state,player2state,player1,player2,count)     #function calling.
    if(cwin!=-1):
        print('\n\033[1m***Match Over***\033[0m')
        break
        
    if count==9:
        print(' ')
        print('\033[1m***TIE***\033[0m')
        break
    
    turn = 1-turn
