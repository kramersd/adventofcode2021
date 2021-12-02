input_file_name = 'aoc_puzzle2_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        depth = 0
        pos = 0
        for l in lines:
            x = l.split(' ')
            if x[0] == 'forward':
                pos += int(x[1])
            elif x[0] == 'up':
                depth -= int(x[1])
            elif x[0] == 'down':
                depth += int(x[1])
        print('depth', depth)
        print('pos', pos)
        print('multipl', depth*pos)


def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        depth = 0
        pos = 0
        aim = 0
        for l in lines:
            x = l.split(' ')
            if x[0] == 'forward':
                pos += int(x[1])
                depth += (int(x[1]) * int(aim))
            elif x[0] == 'up':
                # depth -= int(x[1])
                aim -= int(x[1])
            elif x[0] == 'down':
                # depth += int(x[1])
                aim += int(x[1])
        print('depth', depth)
        print('pos', pos)
        print('aim', aim)
        print('multipl', depth*pos)

part2()