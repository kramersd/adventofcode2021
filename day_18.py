from time import time
from uuid import uuid4
from copy import deepcopy, copy
from math import floor, ceil


# input_file_name = 'aoc_puzzle18_input.txt'
input_file_name = 'sample_day_18.txt'


class SnailFishPair:

    id = None
    left = None
    right = None
    depth = None
    parent = None

    def __init__(self, left, right):
        self.id = uuid4()
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        if not isinstance(other, SnailFishPair):
            return False
        return self.id == other.id

    def __str__(self):
        s = '['
        if self.is_left_a_literal():
            s += str(self.left) + ','
        elif self.left == None:
            s += str('None') + ','
        else:
            s += str('SnailFishPair') + ','
        
        if self.is_right_a_literal():
            s += str(self.right)
        elif self.right == None:
            s += str('None') + ','
        else:
            s += str('SnailFishPair')
        s += ']'
        
        t = str((s, 'd' + str(self.get_depth())))
        return t
    
    def __repr__(self):
        return self.__str__()


    def get_full_string(self):
        s = '['
        if self.is_left_a_literal():
            s += str(self.left) + ','
        elif self.left != None:
            s += self.left.get_full_string() + ','

        if self.is_right_a_literal():
            s += str(self.right)
        elif self.right != None:
            s += self.right.get_full_string()
        
        s += ']'
        return s
    
    # def __repr__(self):
    #     return self.__str__()
        
    def get_left(self):
        return self.left
    
    def set_left(self, left):
        self.left = left
    
    def get_right(self):
        return self.right
    
    def set_right(self, right):
        self.right = right
    
    def is_left_a_literal(self):
        if self.left == None:
            return False
        elif isinstance(self.left, SnailFishPair):
            return False
        elif isinstance(self.left, int):
            return True
        else:
            print('Left - Unknown assignment type', type(self.right))
            return False

    def is_right_a_literal(self):
        if self.right == None:
            return False
        elif isinstance(self.right, SnailFishPair):
            return False
        elif isinstance(self.right, int):
            return True
        else:
            print('Right - Unknown assignment type', type(self.right))
            return False

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
    
    def is_pair(self):
        return self.left != None and self.right != None
    
    def get_id(self):
        return self.id

def p1_generate_nodes(line):
    nodes = []
    all_nodes = []
    for i in line:
        if i == '[':
            snp = SnailFishPair(None, None)
            snp.depth = len(nodes) + 1
            
            if len(nodes) > 0:
                if nodes[len(nodes) - 1].get_left() == None:
                    nodes[len(nodes) - 1].set_left(snp)
                elif nodes[len(nodes) - 1].get_right() == None:
                    nodes[len(nodes) -1 ].set_right(snp)
                snp.set_parent(nodes[len(nodes) - 1])
            nodes.append(snp)
            all_nodes.append(snp)
        elif i not in ['[', ']', ',']:
            snp = nodes[len(nodes) - 1]
            if snp.get_left() == None:
                snp.set_left(int(i))
            elif snp.get_right() == None:
                snp.set_right(int(i))
        elif i == ']':
            nodes.pop(len(nodes) - 1)
    
    return (all_nodes, all_nodes[0])

def p1_explode(root_node):
    print('Start Exploding')

    # Find the max depth node
    max_depth_node = root_node
    min_needed_depth = 4
    
    q = [root_node]
    while len(q) > 0:
        node = q.pop(0)
        left = node.get_left()
        right = node.get_right()

        if isinstance(left, SnailFishPair):
            depth = left.get_depth()
            if depth > min_needed_depth and depth > max_depth_node.get_depth():
                max_depth_node = left
            q.append(left)
        if isinstance(right, SnailFishPair):
            depth = right.get_depth()
            if depth > min_needed_depth and depth > max_depth_node.get_depth():
                max_depth_node = right
            q.append(right)

    if max_depth_node == root_node:
        print('End Exploding - Early')
        return False
    
    print('Max depth Node', max_depth_node)

    # Add left to the first left number
    search_node = copy(max_depth_node)
    while search_node != root_node:
        parent = search_node.get_parent()
        parent_left = parent.get_left()
        
        if parent_left == None:
            print('Problem Found', parent)

        if parent_left == search_node:
            search_node = parent
        else:
            if isinstance(parent_left, int):
                new_num = max_depth_node.get_left() + parent_left
                parent.set_left(new_num)
                break
            elif isinstance(parent_left, SnailFishPair):
                left = parent_left.get_left()
                right = parent_left.get_right()
                if isinstance(right, int):
                    new_num = max_depth_node.get_right() + right
                    parent_left.set_right(new_num)
                    break
                elif isinstance(left, int):
                    new_num = max_depth_node.get_right() + left
                    parent_left.set_right(new_num)
                    break
                else:
                    search_node = right
    
    # Add right to the first right number
    search_node = max_depth_node
    while search_node != root_node:
        parent = search_node.get_parent()
        parent_right = parent.get_right()

        print('********************* Search Node', search_node)
        print('********************* Parent node', parent)

        if parent_right == None:
            print('Problem Found', parent)

        if parent_right == search_node:
            search_node = parent
        else:
            if isinstance(parent_right, int):
                new_num = max_depth_node.get_right() + parent_right
                parent.set_right(new_num)
                break
            elif isinstance(parent_right, SnailFishPair):
                left = parent_right.get_left()
                right = parent_right.get_right()
                if isinstance(left, int):
                    new_num = max_depth_node.get_right() + left
                    parent_right.set_left(new_num)
                    break
                elif isinstance(right, int):
                    new_num = max_depth_node.get_right() + right
                    parent_right.set_left(new_num)
                    break
                else:
                    search_node = left
        
    
    parent = max_depth_node.get_parent()
    parent.set_depth(max_depth_node.get_depth() - 1)
    if parent.get_left() == max_depth_node:
        parent.set_left(0)
    elif parent.get_right() == max_depth_node:
        parent.set_right(0)

    print('End Exploding - Propogated')
    return True


def p1_split(root_node):
    print('Start Splitting')

    node_to_split = None
    parent = None
    is_left = None
    q = [root_node]
    while len(q) > 0:
        node = q.pop(0)
        left = node.get_left()
        right = node.get_right()

        if isinstance(left, int) and left >= 10:
            node_to_split = left
            parent = node
            is_left = True
            break
        elif isinstance(right, int) and right >= 10:
            node_to_split = right
            parent = node
            is_left = False
            break
        if isinstance(left, SnailFishPair):
            q.append(left)
        if isinstance(right, SnailFishPair):
            q.append(right)
    
    if node_to_split != None:        
        new_left = floor(node_to_split / 2.0)
        new_right = ceil(node_to_split / 2.0)
        new_node = SnailFishPair(int(new_left), int(new_right))
        new_node.set_depth(parent.get_depth() + 1)
        new_node.set_parent(parent)
        if is_left:
            parent.set_left(new_node)
        else:
            parent.set_right(new_node)
        return True
    else:
        return False
    

def p1_loop_explode(root_node):
    print('Loop Exploding Start')
    can_explode = True
    while can_explode:
        can_explode = p1_explode(root_node)
        print('after explode', root_node.get_full_string())
    print('Finished Loop Exploding')

def p1_reduce(root_node, all_nodes = None):
    print('----- Reduction Start -----')
    
    print('Reduction FPS', root_node.get_full_string())

    # 1. Explode
    # 2. Split
        # If split causes explode, then you must explode before continuing
    
    print('First Explosion')
    p1_loop_explode(root_node)
    
    
    can_split = True
    while can_split:
        print('Start Loop Splitting')
        can_split = p1_split(root_node)
        print('after split', root_node.get_full_string())
        p1_loop_explode(root_node)


    print('Finished Loop Splitting')
    
    if all_nodes:
        print(all_nodes)
    print(root_node.get_full_string())

    print('Finished Reduction')
    return root_node

def part1():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()
        snailfish_numbers = []

        for l in lines:
            gn = p1_generate_nodes(l.strip())
            rd = p1_reduce(gn[1], all_nodes=gn[0])
            snailfish_numbers.append(rd)

        print('All Lines as strings')
        for i in range(len(snailfish_numbers)):
            print(i, snailfish_numbers[i].get_full_string())

        # for sn in snailfish_numbers():

        snailfish_sum = snailfish_numbers[0]

        print('--------------------- Start Summation --------------------------')
        q = copy(snailfish_numbers[1:])
        i = 0
        while len(q) > 0:
            current_number = q.pop(0)
            print('A', snailfish_sum.get_full_string())
            print('B', current_number.get_full_string())
            
            new_sum = SnailFishPair(snailfish_sum, current_number)
            new_sum.set_depth(0)
            
            snailfish_sum.set_parent(new_sum)
            current_number.set_parent(new_sum)

            print('Before Depth Changes New Sum FPS', new_sum.get_full_string())

            all_nodes = []
            qq = [new_sum]
            while len(qq) > 0:
                temp = qq.pop(0)
                all_nodes.append(temp)
                temp.set_depth(temp.get_depth() + 1)
                left = temp.get_left()
                right = temp.get_right()
                
                if isinstance(left, SnailFishPair):
                    qq.append(left)
                if isinstance(right, SnailFishPair):
                    qq.append(right)
            
            snailfish_sum = p1_reduce(new_sum)
            i += 1
            print('######## ####### FS So Far', snailfish_sum.get_full_string())
        
        print('Final string', snailfish_sum.get_full_string())

        

part1()