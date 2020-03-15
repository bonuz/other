theBoard = { "Top-L": "O", "Top-M": "O", "Top-R": "O",
             "Mid-L": "X", "Mid-M": "X", "Mid-R": " ",
             "Low-L": " ", "Low-M": " ", "Low-R": "X"}

theBoard = { "Top-L": " ", "Top-M": " ", "Top-R": " ",
             "Mid-L": " ", "Mid-M": " ", "Mid-R": " ",
             "Low-L": " ", "Low-M": " ", "Low-R": " "}


def printBoard(board):
    print(board["Top-L"] + "|" + board["Top-M"] + "|" + board["Top-R"])
    print("-+-+-")
    print(board["Mid-L"] + "|" + board["Mid-M"] + "|" + board["Mid-R"])
    print("-+-+-")
    print(board["Low-L"] + "|" + board["Low-M"] + "|" + board["Low-R"])
    print("-+-+-")

turn = "X"
for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ". Move on wich space?")
    move=input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    
printBoard(theBoard)
