from copy import copy, deepcopy
from time import time
from math import pow

input_file_name = 'aoc_puzzle14_input.txt'

def part1():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()
        sequence = []
        pi_rules = {}

        for l in lines:
            if '->' in l:
                temp = l.strip()
                s = temp.split('->')
                pi_rules[s[0].strip()] = s[1].strip()
            elif len(l) > 1:
                temp = l.strip()
                for i in temp:
                    sequence.append(i.strip())
        steps = 10
        old_seq = copy(sequence)
        new_seq = copy(sequence)

        for i in range(steps):
            old_seq = copy(new_seq)
            new_seq = []

            for j in range(len(old_seq) - 1):
                pair = old_seq[j] + old_seq[j + 1]
                new_seq.append(old_seq[j])
                new_seq.append(pi_rules[pair])
            new_seq.append(old_seq[len(old_seq) - 1])
        
        letter_freq = {}
        for i in new_seq:
            if i in letter_freq:
                letter_freq[i] += 1
            else:
                letter_freq[i] = 1
        
        
        min_freq = min(letter_freq.values())
        max_freq = max(letter_freq.values())
        print('Part 1')
        print('Min Freq', min_freq)
        print('Max Freq', max_freq)
        print('Diff', max_freq - min_freq)
        print('Time', time() - t0)
        print(letter_freq)


def part2():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()
        sequence = []
        pi_rules = {}

        for l in lines:
            if '->' in l:
                temp = l.strip()
                s = temp.split('->')
                pi_rules[s[0].strip()] = s[1].strip()
            elif len(l) > 1:
                temp = l.strip()
                for i in temp:
                    sequence.append(i.strip())
        
        old_seq = copy(sequence)

        new_seq = []
        pair_map = {}
        for i in range(len(old_seq) - 1):
            new_pair = old_seq[i] + old_seq[i + 1]
            new_seq.append(old_seq[i] + old_seq[i + 1])
            pair_map[new_pair] = pair_map.get(new_pair, 0) + 1
        
        new_map = deepcopy(pair_map)
        steps = 40

        letter_freq = {}
        for s in sequence:
            letter_freq[s] = letter_freq.get(s, 0) + 1
        
        for i in range(steps):
            old_map = deepcopy(new_map)
            new_map = {}
            for k,v in old_map.items():
                # C   <-- NN
                new_letter = pi_rules[k]
                
                letter_freq[new_letter] = letter_freq.get(new_letter, 0) + v
                
                # Left = N + C => NC
                left_pair = k[0:1] + new_letter

                # Right = C + N => CN
                right_pair = new_letter + k[1:]

                new_map[left_pair] = new_map.get(left_pair, 0) + v
                new_map[right_pair] = new_map.get(right_pair, 0) + v
        
        print('Time', time() - t0)

        min_freq = min(letter_freq.values())
        max_freq = max(letter_freq.values())
        print('Min freq', min_freq)
        print('Max freq', max_freq)
        print('Diff', max_freq - min_freq)

        total_nodes = 0
        for v in new_map.values():
            total_nodes += v
        print('Steps', steps)
        print('Total Nodes', total_nodes)
        print('Expected Nodes', pow(2, steps) * sum(pair_map.values()))


# part1()
part2()