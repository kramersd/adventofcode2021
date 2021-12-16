from time import time
from heapq import heapify, heappop, heappush

input_file_name = 'aoc_puzzle15_input.txt'

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)

    def __repr__(self):
        return str(self.position)
    
    def __lt__(self, other):
        return self.f < other.f

def read_input(lines):
    board = []
    for l in lines:
        row = []
        for c in l:
            temp = c.strip()
            if temp != '':
                row.append(int(temp))
        board.append(row)
    return board

def a_start_search(board, start, end):
    print('Beginning A* search')
    print('Starting point', start)
    print('Ending Point', end)

    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = 0
    
    end_node = Node(None, end)
    end_node.g = 0
    end_node.h = 0
    end_node.f = 0

    open_list = []
    open_list.append(start_node)

    closed_list = []
    heapify(open_list)

    while len(open_list) > 0:
        # Pop the current node with the least f value
        current_node = heappop(open_list)
        closed_list.append(current_node)

        # Exit node found
        if current_node == end_node:
            print('Current is exit node')
            path = []
            current = current_node
            while current is not None:
                path.append(current)
                current = current.parent
            return path[::-1] # Return reversed path
        
        children = []
        #                  N        S     W        E
        cardinal_dirs = [(0,-1), (0,1), (-1,0), (1, 0)]
        for cd in cardinal_dirs:
            new_node_pos = (current_node.position[0] + cd[0], current_node.position[1] + cd[1])
            
            # Out of bounds North or South
            if new_node_pos[0] > len(board) - 1 or new_node_pos[0] < 0:
                continue
            
            # Out of bounds East or West
            if new_node_pos[1] > len(board[0]) - 1 or new_node_pos[1] < 0:
                continue

            new_node = Node(current_node, new_node_pos)
            children.append(new_node)
        
        for child in children:

            if child in closed_list:
                continue

            # Exit node found
            if current_node == end_node:
                print('Child is exit node')
                path = []
                current = current_node
                path.append(child)
                while current is not None:
                    path.append(current)
                    current = current.parent
                return path[::-1] # Return reversed path

            child_x_pos = child.position[0]
            child_y_pos = child.position[1]
            child.g = current_node.g + board[child_x_pos][child_y_pos]

            # Manhattan Distance
           
            dX = abs(child_x_pos - end_node.position[0])
            dY = abs(child_y_pos - end_node.position[1])
            child.h = (dX + dY)
            child.f = child.g + child.h

            # Child is already in the open list
            if child in open_list: 
                idx = open_list.index(child) 
                if child.g < open_list[idx].g:
                    # update the node in the open list
                    open_list[idx].g = child.g
                    open_list[idx].f = child.f
                    open_list[idx].h = child.h
            
            heappush(open_list, child)

def get_total_from_path(board, path):
    total = 0
    for p in path:
        if p.position != (0,0):
            total += board[p.position[0]][p.position[1]]
    return total

def print_path(size, path):
    b = []
    for i in range(size):
        y = []
        for j in range(size):
            y.append('.')
        b.append(y)
    
    for p in path:
        b[p.position[0]][p.position[1]] = 'X'
    

    for i in range(size):
        s = ''
        for j in range(size):
            s += b[i][j] + ' '
        print(s)


def part1():
    with open(input_file_name) as f:
        print('##### Part 1 Begin ######')
        t0 = time()
        lines = f.readlines()
        board = read_input(lines)

        print('IxJ', len(board), len(board[0]))

        start = (0,0)
        end = (len(board) - 1, len(board) - 1)
        path = a_start_search(board, start, end)

        
        print('##### Part 1 Answer ######')
        print('Time', time() - t0)
        print('Len of Path', len(path))

        total = get_total_from_path(board, path)
        
        print('Total', total)

# Takes a long time, but it worked
part1()