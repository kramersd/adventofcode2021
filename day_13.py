from time import time
from copy import deepcopy
input_file_name = 'aoc_puzzle13_input.txt'
# input_file_name = 'temp_13.txt'

def print_board(board):
    for i in range(len(board)):
        s = ''
        for j in range(len(board[0])):
            s += board[i][j]
        print(s)

def part1():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()
        fold_instructions = []
        dots = []
        board = []

        for l in lines:
            if 'fold' in l:
                fold_instructions.append(l.strip())
            elif ',' in l:
                temp = l.strip().split(',')
                dots.append((int(temp[0]), int(temp[1])))
        
        max_x = 0
        max_y = 0
        for i in dots:
            if i[0] > max_y:
                max_y = i[0]
            if i[1] > max_x:
                max_x = i[1]
        max_y += 1
        max_x += 1
        
        for i in range(max_x):
            r = []
            for j in range(max_y):
                r.append('.')
            board.append(r)
        
        for d in dots:
            board[d[1]][d[0]] = '#'
        
        fi = []
        for f in fold_instructions:
            temp = f.split(' ')
            temp_two = temp[2].split('=')
            fi.append((temp_two[0], int(temp_two[1])))

        new_board = []
        f1 = fi.pop(0)
        if f1[0] == 'x':
            print('Folding on X =', f1[1])
            for i in range(len(board)):
                row = []
                for j in range(f1[1]):
                    row.append(board[i][j])
                new_board.append(row)
            for i in range(len(board)):
                for j in range(f1[1] + 1, len(board[0])):
                    if board[i][j] == "#":
                        diff = j - f1[1]
                        new_y = f1[1] - diff
                        new_board[i][new_y] = '#'
        elif f1[0] == 'y':
            print('Folding on Y =', f1[1])
            for i in range(f1[1]):
                new_board.append(board[i])
            
            for i in range(f1[1] + 1, len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '#':
                        diff = i - f1[1]
                        new_x = f1[1] - diff
                        new_board[new_x][j] = '#'
        
        total = 0
        for i in range(len(new_board)):
            for j in range(len(new_board[0])):
                if new_board[i][j] == '#':
                    total += 1

        print('Total Dots after 1 fold', total)
        print('Time', time() - t0)


def part2():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()
        fold_instructions = []
        dots = []
        board = []

        for l in lines:
            if 'fold' in l:
                fold_instructions.append(l.strip())
            elif ',' in l:
                temp = l.strip().split(',')
                dots.append((int(temp[0]), int(temp[1])))
        
        max_x = 0
        max_y = 0
        for i in dots:
            if i[0] > max_y:
                max_y = i[0]
            if i[1] > max_x:
                max_x = i[1]
        max_y += 1
        max_x += 1
        
        for i in range(max_x):
            r = []
            for j in range(max_y):
                r.append('.')
            board.append(r)
        
        for d in dots:
            board[d[1]][d[0]] = '#'
        
        fi = []
        for f in fold_instructions:
            temp = f.split(' ')
            temp_two = temp[2].split('=')
            fi.append((temp_two[0], int(temp_two[1])))

         
        old_board = []
        new_board = deepcopy(board)
        for fold in fi:
            old_board = deepcopy(new_board)
            new_board = []
            f1 = fold
            if f1[0] == 'x':
                print('Folding on X =', f1[1])
                for i in range(len(old_board)):
                    row = []
                    for j in range(f1[1]):
                        row.append(old_board[i][j])
                    new_board.append(row)
                for i in range(len(old_board)):
                    for j in range(f1[1] + 1, len(old_board[0])):
                        if old_board[i][j] == "#":
                            diff = j - f1[1]
                            new_y = f1[1] - diff
                            new_board[i][new_y] = '#'
            elif f1[0] == 'y':
                print('Folding on Y =', f1[1])
                for i in range(f1[1]):
                    new_board.append(old_board[i])
                
                for i in range(f1[1] + 1, len(old_board)):
                    for j in range(len(old_board[0])):
                        if old_board[i][j] == '#':
                            diff = i - f1[1]
                            new_x = f1[1] - diff
                            new_board[new_x][j] = '#'
        
        print_board(new_board)
        # total = 0
        # for i in range(len(new_board)):
        #     for j in range(len(new_board[0])):
        #         if new_board[i][j] == '#':
        #             total += 1

        # print('Total Dots after 1 fold', total)
        print('Time', time() - t0)
       

part2()