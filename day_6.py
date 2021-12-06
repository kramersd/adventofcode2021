input_file_name = 'aoc_puzzle6_input.txt'

def part1():
    with open(input_file_name) as f:
        days = 80
        lantern_fish = []
        lines = f.readlines()
        for l in lines:
            fish_numbers = l.split(',')
            for fn in fish_numbers:
                lantern_fish.append(int(fn.strip()))
        
        for d in range(days):
            print('Day', d)
            print('Total Fish', len(lantern_fish))
            for i in range(len(lantern_fish)):
                fish = lantern_fish[i]
                if fish == 0:
                    lantern_fish.append(8)
                    lantern_fish[i] = 6
                else:
                    lantern_fish[i] -= 1
            print('Total Fish After Spawning', len(lantern_fish))

def part2():
    with open(input_file_name) as f:
        days = 256
        lantern_fish = []
        lines = f.readlines()
        for l in lines:
            fish_numbers = l.split(',')
            for fn in fish_numbers:
                lantern_fish.append(int(fn.strip()))
        
        fish_day_map = {}
        for f in lantern_fish:
            fish_day_map[f] = fish_day_map.get(f, 0) + 1
        
        print('# of Days Elasped', days)
        for d in range(days):
            if d in fish_day_map:
                fish_day_map[d + 7] = fish_day_map.get(d + 7, 0) + fish_day_map[d]
                fish_day_map[d + 9] = fish_day_map.get(d + 9, 0) + fish_day_map[d]
                del fish_day_map[d]
        
        total = 0
        for v in fish_day_map.values():
            total += int(v)
        print('Total', total)

part2()