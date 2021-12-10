import statistics
input_file_name = 'aoc_puzzle10_input.txt'

def p1_is_corrupted(input_str):
    close_for_open = { '(': ')', '[': ']', '{': '}', '<': '>'}

    stack = []
    for c in input_str:
        if c in '({[<':
            stack.append(c)
        elif c in ')}]>':
            if len(stack) == 0:
                return c

            o = stack.pop()
            if close_for_open[o] != c:
                return c
    
    return 'n/a'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()

        bad_characters = []
        for i in range(len(lines)):
            stack = []
            x = p1_is_corrupted(lines[i])
            if x != 'n/a':
                bad_characters.append(x)
            
        scoring = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        syntax_score = 0
        for bc in bad_characters:
            syntax_score += scoring[bc]
        print('Syntax Score', syntax_score)



def p2_is_corrupted(line):
    close_for_open = { '(': ')', '[': ']', '{': '}', '<': '>'}

    stack = []
    for c in line:
        if c in '({[<':
            stack.append(c)
        elif c in ')}]>':
            if len(stack) == 0:
                return ('corrupted', c)

            o = stack.pop()
            if close_for_open[o] != c:
                return ('corrupted', c)
    
    return ('incomplete', stack)


def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        needed_characters = []
        for i in range(len(lines)):
            x = p2_is_corrupted(lines[i])
            if x[0] == 'incomplete':
                unclosed = []
                for j in x[1]:
                    close_for_open = { '(': ')', '[': ']', '{': '}', '<': '>'}
                    unclosed.append(close_for_open[j])
                temp= []
                for un in range(len(unclosed) - 1, -1, -1):
                    temp.append(unclosed[un])
                unclosed = temp
                needed_characters.append(unclosed)

        char_values = { ')': 1, ']': 2, '}': 3, '>': 4}
        line_totals = []
        for n in needed_characters:
            total = 0
            for c in n:
                total = (total * 5) + char_values[c]
            line_totals.append(total)
        
        line_totals.sort()
        print('Median', statistics.median(line_totals))

part1()
part2()
