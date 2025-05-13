board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 5)

def check_win(player):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

turn = 'X'
for _ in range(9):
    print_board()
    move = int(input(f"{turn}'s move (0-8): "))
    if board[move] == ' ':
        board[move] = turn
        if check_win(turn):
            print_board()
            print(f"{turn} wins!")
            break
        turn = 'O' if turn == 'X' else 'X'
else:
    print_board()
    print("It's a tie!")
