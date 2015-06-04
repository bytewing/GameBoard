__author__ = 'narayans'
from gameboard import GameBoard
import time

#this function provides examples of gameboard usage
#this demo illustrates everything you can do with a gameboard
def demo():
    import random
    import time

    #get a reference to the GameBoard
    #you will use this reference to communicate with the gameboard
    gb = GameBoard.get_board()

    #resize it to the specified dimensions
    gb.set_size(6,8)

    row = 3
    col = 4

    #change the color of specified cell
    gb.set_color(row, col, "RED")

    #change the label of the specified cell
    gb.set_label(row, col, "X")

    #Retrieve the name of the color of the specified cell
    c = gb.get_color(row, col)
    print("Cell ", row, col, " is colored ", c)

    #Retrieve the label of the specified cell
    letter = gb.get_label(row, col)
    print("Cell ", row, col, " has label ", letter)

    #Retrieve the number of rows in the board
    max_rows = gb.get_row_count()

    #Retrieve the number of columns in the board
    max_cols = gb.get_column_count()

    #Iterate over the board and assign random letters to the cells
    for row in range(max_rows):
        for col in range(max_cols):
            letter = chr(random.randint(ord('A'), ord('Z')))
            gb.set_label(row, col, letter)
            time.sleep(0.1)

def search():
    gb = GameBoard.get_board()

    word = input("Enter word for which to search: ")

    h = gb.get_row_count()
    w = gb.get_column_count()

    done = False
    for row in range(h):
        for col in range(w):
            done = search_east(gb, row, col, word, 0)
            if done:
                return

def search_east(gb, row, col,  word, index):
    if index == len(word): #matched all letters of word
        return True
    elif col == gb.get_column_count() or word[index] != gb.get_label(row,col): #reached right end of board
        return False
    else: #some letter matches
        c = gb.get_color(row, col)
        gb.set_color(row, col, "GREEN")
        time.sleep(1)
        x = search_east(gb, row, col+1, word, index+1)
        if x == False:
            gb.set_color(row, col, c)
            time.sleep(1)
        return x

def word_search():
    gb = GameBoard.get_board()

    word = input("Enter word for which to search: ")

    h = gb.get_row_count()
    w = gb.get_column_count()

    for row in range(h):
        k = 0
        for col in range(w):
            letter = gb.get_label(row, col)
            if letter == word[k]:
                k += 1

            if k == len(word): #found word
                __highlight_row(row, col, len(word))
                break

def __highlight_row(row, col, k):
    gb = GameBoard.get_board()
    for col in range(col-k+1,col+1):
        gb.set_color(row, col, "YELLOW")

def foo():
    pass

def init_game():
    file = open("Resources/Places.txt", "r")

    lines = []
    for line in file:
        line = line.strip()
        lines.append(line.split())

    h = len(lines)
    w = len(lines[0])

    gb = GameBoard.get_board()
    gb.set_size(h, w)

    for row in range(h):
        for col in range(w):
            letter = lines[row][col]
            gb.set_label(row, col, letter)

    #gb.set_color(0,2,"RED")
    #gb.set_label(0,2,"X")

if __name__ == '__main__':
    GameBoard(11,15)
