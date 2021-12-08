import itertools
import time

input_file_name = 'aoc_puzzle8_input.txt'

sev_seg_nums = {
    '1': {
        'num_segments': 2,
        'frequency': 0
    },
    '4': {
        'num_segments': 4,
        'frequency': 0
    },
    '7': {
        'num_segments': 3,
        'frequency': 0
    },
    '8': {
        'num_segments': 7,
        'frequency': 0
    }
}

# x1 x2 x3 x4 x5 x6 x7
permutations = list(itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']))

def part1():
    with open(input_file_name) as f:
        t0 = time.time()
        lines = f.readlines()
        signal_lines = []

        for l in lines:
            parts = l.split(' | ')
            signal_parts = []
            signal_parts.append(parts[0].split(' '))
            signal_parts.append(parts[1].split(' '))

            signal_lines.append(signal_parts)

        print('Len', len(signal_lines))
        print('Signal Part 0', signal_lines[0])

        for sl in signal_lines:
            # s = [ 10-[], 4-[] ]
            output_signals = sl[1]

            for os in output_signals:
                oss = os.strip()
                for k in sev_seg_nums.keys():
                    if sev_seg_nums[k]['num_segments'] == len(oss):
                        sev_seg_nums[k]['frequency'] += 1

        total = 0
        for k in sev_seg_nums.keys():
            freq = sev_seg_nums[k]['frequency']
            print('(Key, Freq)', (k, freq))
            total += freq
        print('Total', total)
        print('Total time', time.time() - t0)


def part2():
    with open(input_file_name) as f:
        t0 = time.time()
        lines = f.readlines()
        signal_lines = []

        for l in lines:
            parts = l.split(' | ')
            signal_parts = []
            signal_parts.append(parts[0].split(' '))
            signal_parts.append(parts[1].split(' '))

            signal_lines.append(signal_parts)

        print('Len', len(signal_lines))
        print('Signal Part 0', signal_lines[0])

        output_values = []

        for sl in signal_lines:
            # print('SL', sl)
            unique_signals = sl[0]
            output_signals = sl[1]

            for p in permutations:
                good_segment_set = True
                for us in unique_signals:
                    segments = {
                        'x1': p[0],
                        'x2': p[1],
                        'x3': p[2],
                        'x4': p[3],
                        'x5': p[4],
                        'x6': p[5],
                        'x7': p[6]
                    }
                    if test_segment_set(segments, us) == -1:
                        good_segment_set = False
                
                
                if good_segment_set:
                    # out_us = []
                    os_nums = []
                    segments = {
                        'x1': p[0],
                        'x2': p[1],
                        'x3': p[2],
                        'x4': p[3],
                        'x5': p[4],
                        'x6': p[5],
                        'x7': p[6]
                    }
                    # for us in unique_signals:
                    #     out_us.append(test_segment_set(segments, us))

                    for os in output_signals:
                        os_nums.append(test_segment_set(segments, os))
                    output_values.append(os_nums)
        
        total = 0
        for ov in output_values:
            s = ''
            for v in ov:
                s += str(v)
            # print('Output Code', int(s))
            total += int(s)
        print('Total', total)
        print('Time', time.time() - t0)
            

def test_segment_set(segments, input_code):
    numbers = {
        0: ['x1', 'x2', 'x3', 'x5', 'x6', 'x7'],
        1: ['x3', 'x6'],
        2: ['x1', 'x3', 'x4', 'x5', 'x7'],
        3: ['x1', 'x3', 'x4', 'x6', 'x7'],
        4: ['x2', 'x3', 'x4', 'x6'],
        5: ['x1', 'x2', 'x4', 'x6', 'x7'],
        6: ['x1', 'x2', 'x4', 'x5', 'x6', 'x7'],
        7: ['x1', 'x3', 'x6'],
        8: ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7'],
        9: ['x1', 'x2', 'x3', 'x4', 'x6', 'x7'],
    }
    x_codes = []
    for i in sorted(input_code):
        for k,v in segments.items():
            if i == v:
                x_codes.append(k)
    
    x_codes = sorted(x_codes)

    for k,v in sorted(numbers.items()):
        if v == x_codes:
            return k
    return -1

part2()