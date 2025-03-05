# Domenico Valentino
# 2432975
# Part 2 (NOTHING CHANGED FROM PART 1)

import random
import sys
import os

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def tileLabels(n):
    result = []
    for i in range(1, (n**2)):
        result.append(str(i))
    result.append("  ")
    return result

def getNewPuzzle(n):
    labels = tileLabels(n)
    random.shuffle(labels)
    result = []
    for i in range(0, len(labels), n):
        result.append([str(n) if len(n) == 2 else str(n) + " " for n in labels[i:i+n]])
    return result


def findEmptyTile(board): 
    for y in range(len(board)):
        for x in range(len(board[y])):
            if(board[y][x] == "  "):
                return (y, x)


def nextMove(board):
    empty = findEmptyTile(board)
    y = empty[0]
    x = empty[1]

    good = []
    w = " "
    a = " "
    s = " "
    d = " "
    if y < len(board)-1:
        w = "W"
        good.append("w")
    if x < len(board)-1:
        a = "A"
        good.append("a")
    if y > 0:
        s = "S"
        good.append("s")
    if x > 0:
        d="D"
        good.append("d")
    
    
    while True:
        print(f"                          ({w})")
        print(f"Enter WASD (or QUIT): ({a}) ({s}) ({d})")

        ans = input("> ")
        if ans.lower() == "quit":
            print("quitter, ok then, I see how it is")
            sys.exit()
        if ans.lower() in good:
            return(ans)

def makeMove(board, move):
    y, x = findEmptyTile(board)
    print(move)
    if move == "w":
        board[y][x] = board[y+1][x]
        board[y+1][x] = "  "
    elif move == "a":
        board[y][x] = board[y][x+1]
        board[y][x+1] = "  "
    elif move == "s":
        board[y][x] = board[y-1][x]
        board[y-1][x] = "  "
    elif move == "d":
        board[y][x] = board[y][x-1]
        board[y][x-1] = "  "
    return board

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def __main__():
    clearScreen()
    print("Welcome to the sliding puzzle game!")
    print("Use W/A/S/D to move a tile into the empty space, or QUIT to exit.")

    n = int(input("Enter the board dimension (3 or 4 recommended): "))
    board = getNewPuzzle(n)
    clearScreen()
    displayBoard(board)

    limit = 31 if n == 3 else (80 if n == 4 else 999)
    for _ in range(limit):
        move = nextMove(board)
        board = makeMove(board, move)
        clearScreen()
        displayBoard(board)
        flat_board = [tile for row in board for tile in row]
        if flat_board == tileLabels(n):
            print("Congratulations! You solved the puzzle!")
            break
    else:
        print("Best of luck next time!")

if __name__ == "__main__":
    __main__()