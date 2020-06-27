from IPython.display import clear_output

def play_game():
    board=["#"," "," "," "," "," "," "," "," "," "]
    print("Welcome to Tic Tac Toe")
    p1=player_input()
    p2=""
    if p1=="X":
        p2="O"
    elif p1=="O":
        p2="X"
    x=1
    display_board(board)
    while True:
        while x <= len(board):
            position=position_choice(board)
            if x%2==1:
                marker=p1
            else:
                marker=p2
            place_marker(board, marker, position)
            display_board(board)
            if win_check(board)==True:
                if(x%2==1):
                    print("Player 1 has won!!")
                else:
                    print("Player 2 has won!!")
                break
            if full_board_check(board):
                print("It's a tie!!")
                break
            x+=1
        if replay():
            board=["#"," "," "," "," "," "," "," "," "," "]
        else:
            break     
        
def display_board(board):
    clear_output()
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])

def player_input():
    while True:
        print("Player 1 : Choose X or O")
        choice=input().upper()
        if(choice=="X" or choice=="O"):
            return choice
        else:
            print("Invalid choice.Try again")
        
def space_check(board, position):
    
    return board[position]==" "
    
def position_choice(board):
    
    while True:
        position = int(input('enter a number for your position:(1-9)'))
        if space_check(board,position) and position >=1 and position <=10:
            break
        else:
            print("Invalid position!!\nTry again")
    return position
    
def full_board_check(board):
    for x in board:
        if x==" ":
            return False
    return True

def place_marker(board, marker, position):
    if type(position) is int:
        board[position]=marker

def win_check(board):
    
    if board[1]==board[2] and board[2]==board[3] and board[1]!=" " and board[2]!=" " and board[3]!=" ":
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[4]!=" " and board[5]!=" " and board[6]!=" ":
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[7]!=" " and board[8]!=" " and board[9]!=" ":
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[1]!=" " and board[4]!=" " and board[7]!=" ":
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[2]!=" " and board[5]!=" " and board[8]!=" ":
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[3]!=" " and board[6]!=" " and board[9]!=" ":
        return True
    elif board[1]==board[5] and board[5]==board[9] and board[1]!=" " and board[5]!=" " and board[9]!=" ":
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[3]!=" " and board[5]!=" " and board[7]!=" ":
        return True
    else:
        return False
        
    
def replay():
    print("Do you want to play another game?(yes or no)")
    answer=input()
    if answer=="yes":
        return True
    elif answer=="no":
        return False
    

play_game()