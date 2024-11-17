import os
def drawboard(spots):
    board=(f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def checkturn(turn):
    if turn %2==0:
        return "O"
    else:
        return "X"
    
def checkwin(spots):
    if(spots[1]==spots[2]==spots[3])\
    or (spots[4]==spots[5]==spots[6])\
    or (spots[7]==spots[8]==spots[9]):
        return True
    elif (spots[1]==spots[4]==spots[7])\
    or (spots[2]==spots[5]==spots[8])\
    or (spots[3]==spots[6]==spots[9]):
        return True
    elif (spots[1]==spots[5]==spots[9])\
    or (spots[3]==spots[5]==spots[7]):
        return True
    else:
        return False

    
spots={1:"1", 2:"3", 3:"3", 4:"4",5:"5", 6:"6", 7:"7", 8:"8",9:"9"}

playing = True
complete=False
turn = 0
prevturn=-1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    drawboard(spots)
    print("Player" + str((turn % 2) + 1) + "'s turn: Pick your sport or press q to quit")
    choice = input()
    if choice=="q":
        playing=False
    elif str.isdigit(choice) and int(choice) in spots:

        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)]= checkturn(turn)
    if checkwin(spots):
        playing, complete = False, True
    if turn>8:
        playing=False

os.system('cls' if os.name == 'nt' else 'clear')
drawboard(spots)

if complete:
    if checkturn(turn) =="X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("Its a tie")
