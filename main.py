import random
import copy

def generate_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def remove_numbers(board, num_to_remove):
    empty_board = board
    for _ in range(num_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while empty_board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        
        removed_number = empty_board[row][col]
        empty_board[row][col] = 0
        # solutions = solve_sudoku(board)

        # if count_solutions(solutions) != 1:
        #     board[row][col] = removed_number 

def generate_sudoku_board():
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    
    return board    

def print_sudoku_board(board):

    horizontal_line = "┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓"
    separator = "┠───┼───┼───╂───┼───┼───╂───┼───┼───┨"
    horizontal_line_end = "┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛"

    print(horizontal_line)
    
    for i in range(9):
        row = "┃ "
        for j in range(9):
            if board[i][j] == 0:
                row += f" {board[i][j]} "
            else: 
                row += f" {board[i][j]} "
            if (j + 1) % 3 == 0 and j != 8:
                row += " ┃ "
        row += " ┃"
        print(row)
        
        if (i + 1) % 3 == 0 and i != 8:
            print(separator)
    
    print(horizontal_line_end)


def generate_sudoku_game(board):
    remove_numbers(board, random.randint(40,55))
    return board

def end_game(board):
    print("Game ended. Here is the complete board:")
    print_sudoku_board(board)

# Example usage
sudoku_board = generate_sudoku_board()
game = copy.deepcopy(sudoku_board)
game_board = generate_sudoku_game(game)
print_sudoku_board(game_board)
print_sudoku_board(sudoku_board)
# print_sudoku_board(game)
# print_sudoku_board(sudoku_board)


