input_file_name = 'aoc_puzzle11_input.txt'

def print_octopuses(octopuses):
    print('-------Octopuses-------')
    for oc in octopuses:
        so = ''
        for c in oc:
            if c >= 10:
                c = hex(c).upper()[2:]
            so += str(c)
        print(so)

def p1_increment_tile(octopuses, i, j, remaining_positions, already_flashed):
    if (i,j) not in already_flashed:
        octopuses[i][j] += 1
        if octopuses[i][j] > 9:
            remaining_positions.insert(1, (i,j))
    

def p1_increment_nearby(p, octopuses, remaining_positions, already_flashed):
    length = len(octopuses[0])

    i = p[0]
    j = p[1]
    total_flashes = 0

    if octopuses[i][j] > 9:
        total_flashes += 1
        octopuses[i][j] = 0
        already_flashed.append((i,j))

        # North
        if i - 1 >= 0:
            p1_increment_tile(octopuses, i - 1, j, remaining_positions, already_flashed)

            # North West
            if j - 1 >= 0:
                p1_increment_tile(octopuses, i - 1, j - 1, remaining_positions, already_flashed)
            
            # North East
            if j + 1 < length:
                p1_increment_tile(octopuses, i - 1, j + 1, remaining_positions, already_flashed)

        # South
        if i + 1 < length:
            p1_increment_tile(octopuses, i + 1, j, remaining_positions, already_flashed)

            # South West
            if j - 1 >= 0:
                p1_increment_tile(octopuses, i + 1, j - 1, remaining_positions, already_flashed)
            
            # South East
            if j + 1 < length:
                p1_increment_tile(octopuses, i + 1, j + 1, remaining_positions, already_flashed)

        # West
        if j - 1 >= 0:
            p1_increment_tile(octopuses, i, j - 1, remaining_positions, already_flashed)
            
        # East
        if j + 1 < length:
            p1_increment_tile(octopuses, i, j + 1, remaining_positions, already_flashed)
        
    return total_flashes

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        octopuses = []
        for l in lines:
            row = []
            for c in l:
                if c != '\n':
                    row.append(int(c.strip()))
            octopuses.append(row)
    
    # 100 Steps
    max_steps = 100
    total_flashes = 0
    for s in range(max_steps):
        
        all_positions = []
        remaining_positions = []
        length = len(octopuses)
        width = len(octopuses[0])
        for i in range(length): #rows
            for j in range(width): #columns
                all_positions.append((i,j))
                remaining_positions.append((i, j))
        
        for p in all_positions:
            octopuses[p[0]][p[1]] += 1

        already_flashed = []
        while len(remaining_positions) > 0:
            p = remaining_positions.pop(0)
            total_flashes += p1_increment_nearby(p, octopuses, remaining_positions, already_flashed)

    print('Total Flashes in 100 steps:', total_flashes)
            
            
def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        octopuses = []
        for l in lines:
            row = []
            for c in l:
                if c != '\n':
                    row.append(int(c.strip()))
            octopuses.append(row)
    
    total_flashes = 0
    step = 0
    while True:
        step += 1
        all_positions = []
        remaining_positions = []
        length = len(octopuses)
        width = len(octopuses[0])
        for i in range(length): #rows
            for j in range(width): #columns
                all_positions.append((i,j))
                remaining_positions.append((i, j))
        
        for p in all_positions:
            octopuses[p[0]][p[1]] += 1

        already_flashed = []
        while len(remaining_positions) > 0:
            p = remaining_positions.pop(0)
            total_flashes += p1_increment_nearby(p, octopuses, remaining_positions, already_flashed)
        
        if len(already_flashed) == 100:
            print('Step', step)
            return 

     
part2()