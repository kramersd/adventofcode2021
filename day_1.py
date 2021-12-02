input_file_name = 'aoc_puzzle1_input.txt'

def part1():
    with open(input_file_name) as f:
        increasing = -1
        prev = 0
        lines = f.readlines()
        print('Total lines', len(lines))
        for i in lines:
            if int(i) > prev:
                increasing += 1
            prev = int(i)
        print('Increasing', increasing)


def part2():
    with open(input_file_name) as f:
        increasing = -1
        prev = 0
        lines = f.readlines()
        for i in range(1,len(lines) - 1):
            sliding_sum = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
            if sliding_sum > prev:
                increasing += 1
            prev = sliding_sum
        print('Increasing', increasing)

part2()