input_file_name = 'aoc_puzzle9_input.txt'

def p1_test_row(i, j, board):
    if i == 0:
        return [board[i + 1][j]]
    elif i == len(board) - 1:
        return [board[i - 1][j]]
    else:
        return [board[i - 1][j], board[i + 1][j]]


def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        board = []
        for l in lines:
            row = []
            p = l.strip()
            for i in p:
                row.append(int(i))
            board.append(row)
        
        lowers = []
        row_pieces = []
        column_pieces = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if j == 0:
                    row_pieces = p1_test_row(i, j, board)
                    column_pieces = [board[i][j + 1]]
                elif j == len(board[i]) - 1:
                    row_pieces = p1_test_row(i, j, board)
                    column_pieces = [board[i][j - 1]]
                else:
                    row_pieces = p1_test_row(i, j, board)
                    column_pieces = [board[i][j - 1], board[i][j + 1]]
                    
                x = row_pieces + column_pieces
                is_lower = True
                
                for k in x:
                    if board[i][j] >= k:
                        is_lower = False
                if is_lower:
                    lowers.append(board[i][j] + 1)

        print('Lowest Point Sum: ', sum(lowers))

            
def p2_flood_fill(board, master_insides, point, positions):
    q = [] # set Q to empty queue
    q.append(point) # add node to the end of Q
    inside = []
    while len(q) != 0:
        n = q.pop(0)
        if board[n[0]][n[1]] != 9 and (n[0], n[1]) not in inside:
            if (n[0], n[1]) in positions:
                positions.remove((n[0], n[1]))
            inside.append( (n[0], n[1]) )
            if n[1] - 1 > 0:
                q.append( (n[0], n[1] - 1) ) # west
            if n[1] + 1 < len(board[0]) - 1:
                q.append( (n[0], n[1] + 1) ) # east
            if n[0] - 1 > 0:
                q.append( (n[0] - 1, n[1]) ) # west
            if n[0] + 1 < len(board[0]):
                q.append( (n[0] + 1, n[1]) ) # south
        
    if len(inside) != 0:
        master_insides.append(inside)
    
    return master_insides


def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        board = []
        for l in lines:
            row = []
            p = l.strip()
            for i in p:
                row.append(int(i))
            board.append(row)

        positions = []
        for i in range(len(board)): # rows
            for j in range(len(board[0])): # columns
                if board[i][j] != 9:
                    positions.append((i,j))

        master_insides = []
        while len(positions) != 0:
            pos = positions.pop(0)
            master_insides = p2_flood_fill(board, master_insides, pos, positions)
        
        lens_of_mis = []
        for mi in master_insides:
            lens_of_mis.append(len(mi))
        lens_of_mis.sort(reverse = True)

        x = 1
        for i in range(3):
            print('Len',i, lens_of_mis[i])
            x *= lens_of_mis[i]
        print('X', x)

part2()