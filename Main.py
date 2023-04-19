def print_board(board):
  print("-------------")
  for row in board:
    print("|", row[0], "|", row[1], "|", row[2], "|")
    print("-------------")


def check_win(board):
  # winner
  # rows
  
  for row in board:
    if row[0] == row[1] == row[2] != ' ':
      return True
      
  # colums
  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] != ' ':
      return True

  # diagonals
  if board[0][0] == board[1][1] == board[2][2] != ' ' or  board[0][2] == board[1][1] == board[2][0] != ' ':
    return True

  return False

def play_game():
  board = [[' ', ' ', ' '], [' ', ' ', ' '], [ ' ',  ' ', ' ']]
  player = 'X'
  print_board(board)

  while True:
    row = int(input("Enter row number (1-3)")) - 1
    col = int(input("Enter column number (1-3)")) - 1

  if board[row][col] == ' ':
    board[row][col] = player
  else:
    print("That space is alredy taken!")
    

  print_board(board)

  if check_win(board):
    print(f"Player {player} wins!")
  # break
  elif all([all(row) for row in board]):
    print("It's a Tie")
    # break

  player = '0' if player == 'X' else 'X'

if __name__ == '__main__':
  play_game()
