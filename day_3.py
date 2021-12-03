input_file_name = 'aoc_puzzle3_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        x = {}
        gamma = ''
        epsilon = ''
        length = 0
        for l in lines:
            length = len(l)
            for i in range(len(l)):
                if l[i] == '\n':
                    continue
                if i not in x:
                    x[i] = {}
                if l[i] not in x[i]:
                    x[i][l[i]] = 1
                else:
                    x[i][l[i]] += 1
        print(x)
        for i in range(length):
            if x[i]['0'] > x[i]['1']:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        print('Gamma (2)', gamma)
        print('Epsilon (2)', epsilon)
        print('Gamma (10)', int(gamma, 2))
        print('Epsilon (10)', int(epsilon, 2))
        print('Product', int(gamma, 2) * int(epsilon, 2))

def p2_mostCommon(numbers):
    pos = 0
    while len(numbers) > 1:
        x = {}
        print('Numbers Length', len(numbers))
        print('Position', pos)
        for l in numbers:
            for i in range(len(l)):
                if l[i] == '\n':
                    continue
                if i not in x:
                    x[i] = {}
                if l[i] not in x[i]:
                    x[i][l[i]] = 1
                else:
                    x[i][l[i]] += 1
        
        
        if '0' not in x[pos]:
            most_common = '1'
        elif '1' not in x[pos]:
            most_common = '0'
        elif x[pos]['0'] > x[pos]['1']:
            most_common = '0'
        else:
            most_common = '1'
        z = []
        for l in numbers:
            if l[pos] == most_common:
                z.append(l)
        
        pos += 1
        numbers = z

    return numbers

def p2_leastCommon(numbers):
    pos = 0
    while len(numbers) > 1:
        x = {}
        print('Numbers Length', len(numbers))
        print('Position', pos)
        for l in numbers:
            for i in range(len(l)):
                if l[i] == '\n':
                    continue
                if i not in x:
                    x[i] = {}
                if l[i] not in x[i]:
                    x[i][l[i]] = 1
                else:
                    x[i][l[i]] += 1
        
        
        if '0' not in x[pos]:
            least_common = '1'
        elif '1' not in x[pos]:
            least_common = '0'
        elif x[pos]['0'] > x[pos]['1']:
            least_common = '1'
        else:
            least_common = '0'
        z = []
        for l in numbers:
            if l[pos] == least_common:
                z.append(l)
        
        pos += 1
        numbers = z

    return numbers


def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        numbers = lines

        oxy = p2_mostCommon(numbers)
        co2 = p2_leastCommon(numbers)

        print('Oxy', oxy)
        print('Co2', co2)

        print('Oxy (Base 10)', int(oxy[0], 2))
        print('Co2 (Base 10)', int(co2[0], 2))
        print('Product', int(oxy[0], 2) * int(co2[0], 2))
part2()