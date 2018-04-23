from random import randint
import sys

board = []

for x in range(5): #create a 5x5 board
  board.append(["O"] * 5)

def print_board(board): 
  for row in board:
    print(" ".join(row))

print_board(board) #print the board for the player to see

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board) #create the random location of the battleship
ship_col = random_col(board)


for turn in range(4): #sets number of turns for the game
    print("Guess row: (0-4)")
    guess_row = int(sys.stdin.readline()) #reads the users input and sets it as an integer
    print("Guess column: (0-4)")
    guess_col = int(sys.stdin.readline())

    if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sunk my battleship!")
      break
    else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Oops, that's not even in the ocean.")
      elif(board[guess_row][guess_col] == "X"):
        print("You guessed that one already.")
      else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X" #change the board position to a 'miss' 
    if turn == 3: #checks your turn count and ends the game
      print("Game Over")
    print("turn", turn + 1)
    print_board(board)
