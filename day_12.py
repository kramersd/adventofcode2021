from copy import copy
from time import time

input_file_name = 'aoc_puzzle12_input.txt'

def part1():
    with open(input_file_name) as f:
        t0 = time()
        nodes = {}
        all_keys = set()
        lines = f.readlines()
        for l in lines:
            pairs = l.split('-')
            p1 = pairs[0].strip()
            p2 = pairs[1].strip()
            if p1 in nodes:
                nodes[p1].append(p2)
            else:
                nodes[p1] = [p2]
            if p1 not in all_keys:
                all_keys.add(p1)
            if p2 not in all_keys:
                all_keys.add(p2)
        
        for ak in all_keys:
            if ak not in nodes:
                nodes[ak] = []
        
        for k,v in nodes.items():
            for i in v:
                if k not in nodes[i]:
                    nodes[i].append(k)
        
        q = []
        for i in nodes['start']:
            q.append(['start', i])
        
        paths = []
        while len(q) > 0:
            next = q.pop(0)
            next_node = next[len(next) - 1]
            did_continue = False
           
            for n in nodes[next_node]:
                if n == 'end':
                    temp = copy(next)
                    temp.append(n)
                    paths.append(temp)
                elif not n.isupper() and n not in next:
                    temp = copy(next)
                    temp.append(n)
                    q.append(temp)
                    did_continue = True
                elif n.isupper():
                    temp = copy(next)
                    temp.append(n)
                    q.append(temp)
                    did_continue = True
            
            if did_continue == False:
                temp = copy(next)
                temp.append('N/A')
                paths.append(temp)
        
        print('# Paths', len(paths))
        j = 0
        for p in paths:
            if not 'N/A' in p:
                j += 1
        print('Viable Paths', j)
        print('Elasped Time', time() - t0)


def part2():
    with open(input_file_name) as f:
        t0 = time()
        nodes = {}
        all_keys = set()
        lines = f.readlines()
        for l in lines:
            pairs = l.split('-')
            p1 = pairs[0].strip()
            p2 = pairs[1].strip()
            if p1 in nodes:
                nodes[p1].append(p2)
            else:
                nodes[p1] = [p2]
            if p1 not in all_keys:
                all_keys.add(p1)
            if p2 not in all_keys:
                all_keys.add(p2)
        
        for ak in all_keys:
            if ak not in nodes:
                nodes[ak] = []
        
        for k,v in nodes.items():
            for i in v:
                if k not in nodes[i]:
                    nodes[i].append(k)
        
        q = []
        for i in nodes['start']:
            q.append(('XXX', ['start', i]))
        
        paths = []
        while len(q) > 0:
            f = q.pop()
            next = f[1]
            next_node = next[len(next) - 1]

            # ( 'sm', [<steps>] )
            for n in nodes[next_node]:
                if n == 'end':
                    temp = copy(next)
                    temp.append(n)
                    paths.append(temp)
                elif not n.isupper() and n not in next:
                    temp = copy(next)
                    temp.append(n)
                    if f[0] != 'XXX':
                        q.append((f[0], temp))
                    else:
                        q.append(('XXX', temp))
                elif not n.isupper() and n in next and f[0] == 'XXX' and n != 'start':
                    temp = copy(next)
                    temp.append(n)
                    q.append((n, temp))
                elif n.isupper():
                    temp = copy(next)
                    temp.append(n)
                    if f[0] != 'XXX':
                        q.append((f[0], temp))
                    else:
                        q.append(('XXX', temp))
        
        print('# Paths', len(paths))
        j = 0
        for p in paths:
            if not 'N/A' in p:
                j += 1
        print('Viable Paths', j)
        print('Elasped Time', time() - t0)

part2()