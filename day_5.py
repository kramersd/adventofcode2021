import json

input_file_name = 'aoc_puzzle5_input.txt'

def part1():
    with open(input_file_name) as f:
        print('Part 1')
        positions = {}
        lines = f.readlines()
        x_and_y = []
        for l in lines:
            a = l.split(' ')
            pair_one = a[0].split(',')
            pair_two = a[2].split(',')
            pair_one.extend(pair_two)
            x_and_y.append(pair_one)
        
        for p in x_and_y:
            x1 = int(p[0])
            y1 = int(p[1])
            x2 = int(p[2])
            y2 = int(p[3].strip())
            if x1 == x2:
                start = min(int(y1), int(y2))
                end = max(int(y1), int(y2))
                for i in range(start, end + 1):
                    positions[(x1, i)] = positions.get((x1, i), 0) + 1
            if y1 == y2:
                start = min(int(x1), int(x2))
                end = max(int(x1), int(x2))
                for i in range(start, end + 1):
                    positions[(i, y1)] = positions.get((i, y1), 0) + 1
            
        answer = 0
        for p in positions.values():
            if int(p) >= 2:
                answer += 1
        print('# of Pos Greater than 2->', answer)



def part2():
    with open(input_file_name) as f:
        print("Part 2")
        positions = {}
        lines = f.readlines()
        x_and_y = []
        for l in lines:
            a = l.split(' ')
            pair_one = a[0].split(',')
            pair_two = a[2].split(',')
            pair_one.extend(pair_two)
            x_and_y.append(pair_one)
        
        for p in x_and_y:
            x1 = int(p[0])
            y1 = int(p[1])
            x2 = int(p[2])
            y2 = int(p[3].strip())
            if x1 == x2:
                start = min(y1, y2)
                end = max(y1, (y2))
                for i in range(start, end + 1):
                    positions[(x1, i)] = positions.get((x1, i), 0) + 1
            elif y1 == y2:
                start = min(x1, x2)
                end = max(x1, x2)
                for i in range(start, end + 1):
                    positions[(i, y1)] = positions.get((i, y1), 0) + 1
            else:
                start_x = 0
                end_x = 0
                temp_y = 0
                down = False

                if x1 < x2:
                    start_x = x1
                    end_x = x2
                    temp_y = y1
                    if y1 > y2:
                        down = True
                    else:
                        down = False
                else:
                    start_x = x2
                    end_x = x1
                    temp_y = y2
                    if y2 > y1:
                        down = True
                    else:
                        down = False

                for i in range(start_x, end_x + 1):
                    positions[(i, temp_y)] = positions.get((i, temp_y), 0) + 1
                    if down:
                        temp_y -= 1
                    else:
                        temp_y += 1
        
        answer = 0
        for p in positions.values():
            if int(p) >= 2:
                answer += 1
        print('# of Pos Greater than 2 ->', answer)

part2()