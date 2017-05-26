board = [" " for i in range(9)]

def PrintBoard():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

PrintBoard()

while True:
    choice = int(input("Enter your move (1-9): "))

    if choice < 1 or choice > 9:
        print()
        print("Invalid choice")
        PrintBoard()
        continue

    if board[choice - 1] == " ":
        board[choice -1] = "X"
    else:
        print()
        print("That space is taken!")

    PrintBoard()

