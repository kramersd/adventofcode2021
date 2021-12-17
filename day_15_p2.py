from time import time
from heapq import heapify, heappop, heappush

# input_file_name = 'aoc_puzzle15_input.txt'
input_file_name = 'sample_day_15.txt'

def p2_read_input(lines):
    board = []
    for l in lines:
        row = []
        for c in l:
            temp = c.strip()
            if temp != '':
                row.append(int(temp))
        board.append(row)
    
    new_board = [[-1 for i in range(len(board) * 5)] for i in range(len(board) * 5)]

    print(new_board[0])

def part2():
    with open(input_file_name) as f:
        print('##### Part 2 Begin ######')
        t0 = time()
        lines = f.readlines()
        board = p2_read_input(lines)
        
        print('##### Part 2 Answer ######')
        print('Time', time() - t0)

part2()