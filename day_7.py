input_file_name = 'aoc_puzzle7_input.txt'
import time


def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        init_pos = []
        for i in lines:
            init_pos = i.split(',')
        for j in range(len(init_pos)):
            init_pos[j] = int(init_pos[j].strip())

        m = {}
        for i in range(1, max(init_pos) + 1):
            for p in init_pos:
                m[i] = m.get(i, 0) + abs(p - i)

        n = sorted(m.items(), key=lambda item: item[1])
        print('(Position, Total Cost)', n[0])
        
def part2():
    
    with open(input_file_name) as f:
        t0 = time.time()
        lines = f.readlines()
        init_pos = []
        for i in lines:
            init_pos = i.split(',')
        for j in range(len(init_pos)):
            init_pos[j] = int(init_pos[j].strip())
        
        m = {}
        for i in range(1, max(init_pos) + 1):
            for p in init_pos:
                diff = abs(p - i)
                t = 0
                for k in range(1, diff + 1):
                    t += k
                m[i] = m.get(i, 0) + t

        n = sorted(m.items(), key=lambda item: item[1])
        print('Total time', time.time() - t0)
        print('(Position, Total Cost)', n[0])

part2()