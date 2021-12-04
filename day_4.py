input_file_name = 'aoc_puzzle4_input.txt'
import json

def p1_apply(move, boards):
    for b in boards:
        for row in b:
            for i in range(len(row)):
                if row[i] == move:
                    row[i] = 'X'
    return boards

def p1_check_hor_win(boards):
    winning_row = False
    for b in boards:
        for row in b:
            winning_row = True
            for column in row:
                if column != 'X':
                    winning_row = False
            if winning_row == True:
                return [True, b]
    return [winning_row, b]

def p1_check_ver_win(boards):
    winning_column = False
    for b in boards:
        for i in range(len(b)):
            winning_column = True
            for j in range(len(b[i])):
                if b[j][i] != 'X':
                    winning_column = False
            if winning_column == True:
                return [True, b]
    return [winning_column, b]

def p1_sum_all_non_marked(board):
    s = 0
    for row in board:
        for col in row:
            if col != 'X':
                s += int(col)
    return s

def part1():
    with open(input_file_name) as f:
        mp = {}
        boards = []
        lines = f.readlines()
        moves = lines[0].split(',')
        for i in range(2,len(lines),6):
            b = []
            for j in range(5):
                p = lines[j+i].split(' ')
                q = []
                for k in p:
                    if k != '':
                        q.append(k.strip())
                
                b.append(q)
            boards.append(b)
            
        print('Total Boards', len(boards))
        print('Moves', moves)

        for m in moves:
            boards = p1_apply(m, boards)
            x = p1_check_hor_win(boards)
            y = p1_check_ver_win(boards)
            if (x[0]):
                print('Vert Win')
                print('Move', m)
                print('Winning board', x[1])
                s = p1_sum_all_non_marked(x[1])
                print('Sum Non Marked', s)
                print('Sum * Move', int(s)*int(m))
                break
            if (y[0]):
                print('Hor Win')
                print('Move', m)
                print('Winning Board', y[1])
                s = p1_sum_all_non_marked(y[1])
                print('Sum Non Marked', s)
                print('Sum * Move', int(s)*int(m))
                break

#######################################################################################################################################

def p2_apply(move, boards):
    for b in  boards:
        for row in b:
            for i in range(len(row)):
                if row[i] == move:
                    row[i] = 'X'
    return boards

def p2_check_hor_win(boards):
    winning_row = False
    board_num = -1
    b = []
    for b in boards:
        board_num += 1
        for row in b:
            winning_row = True
            for column in row:
                if column != 'X':
                    winning_row = False
            if winning_row == True:
                return [True, b, board_num]
    return [winning_row, b, board_num]

def p2_check_ver_win(boards):
    winning_column = False
    board_num = -1
    b = []
    for b in boards:
        board_num += 1
        for i in range(len(b)):
            winning_column = True
            for j in range(len(b[i])):
                if b[j][i] != 'X':
                    winning_column = False
            if winning_column == True:
                return [True, b, board_num]
    return [winning_column, b, board_num]

def p2_sum_all_non_marked(board):
    s = 0
    for row in board:
        for col in row:
            if col != 'X':
                s += int(col)
    return s

def part2():
    with open(input_file_name) as f:
        boards = []
        lines = f.readlines()
        moves = lines[0].split(',')
        for i in range(2,len(lines),6):
            b = []
            for j in range(5):
                p = lines[j+i].split(' ')
                q = []
                for k in p:
                    if k != '':
                        q.append(k.strip())
                
                b.append(q)
            boards.append(b)
            
        print('Total Boards', len(boards))
        print('Moves', moves)
        for m in moves:
            boards = p2_apply(m, boards)
            last_board = None
            while True:
                x = p2_check_hor_win(boards)
                if x[0] != True:
                    break
                else:
                    last_board = x[1]
                    boards.pop(x[2])

            while True:
                y = p2_check_ver_win(boards)
                if y[0] != True:
                    break
                else:
                    last_board = y[1]
                    boards.pop(y[2])
                
            if last_board != None:
                print('Last Move', m)
                print('Last Board', last_board)
                s = p1_sum_all_non_marked(last_board)
                print('Sum Non Marked', s)
                print('Sum * Move', int(s)*int(m))

# part1()
part2() # Look for the last line logged in the console for answer after executing code
