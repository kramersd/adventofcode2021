from time import time
from copy import copy

input_file_name = 'aoc_puzzle17_input.txt'
# input_file_name = 'day_17_sample.txt'


def p1_within_x(pos, x_min, x_max):
    if pos[0] >= x_min and pos[0] <= x_max:
        return True
    return False

def p1_within_y(pos, y_min, y_max):
    if pos[1] < 0:
        if abs(pos[1]) >= abs(y_min) and abs(pos[1]) <= abs(y_max):
            return True
    if pos[1] >= y_min and pos[1] <= y_max:
        return True
    return False

def p1_past_target_x(pos, x_max):
    if pos[0] > x_max:
        return True
    return False

def p1_past_target_y(pos, y_max):
    if y_max < 0 and pos[1] >= 0:
        return False
    
    if y_max < 0 and pos[1] > y_max:
        return False

    if pos[0] > y_max:
        return True
    return False

def part1():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()
        x_min = 0
        x_max = 0
        y_min = 0
        y_max = 0

        all_x = []
        all_y = []
        for l in lines:
            pieces = l.split(' ')
            x_pieces = pieces[2].split('..')
            
            all_x.append(x_pieces[0].split('=')[1])
            all_x.append(x_pieces[1].split(',')[0])

            y_pieces = pieces[3].split('..')
            
            all_y.append(y_pieces[0].split('=')[1])
            all_y.append(y_pieces[1].split(',')[0])
            
            x_min = int(min(all_x))
            x_max = int(max(all_x))

            y_min = int(min(all_y))
            y_max = int(max(all_y))

            if y_min < 0 and y_max < 0:
                temp = y_max
                y_max = y_min
                y_min = temp
        
        print(x_min, x_max)
        print(y_min, y_max)
        
        starting_velocitys = []
        
        max_range_to_check = 500
        for i in range(max_range_to_check):
            for j in range(-max_range_to_check, max_range_to_check):
                if (i,j) != (0,0):
                    starting_velocitys.append((i,j))
        
        paths_that_hit = []
        for vel in starting_velocitys:

            vel_list = []
            vel_list.append(vel[0])
            vel_list.append(vel[1])
            position = [0,0]
            traced_path = [(0,0)]
            
            while not p1_past_target_x(position, x_max) and not p1_past_target_y(position, y_max):
                if vel_list[1] < 0:
                    position[0] += vel_list[0]
                    position[1] += vel_list[1]
                else:
                    position[0] += vel_list[0]
                    position[1] += vel_list[1]

                new_position = copy(position)
                traced_path.append((new_position[0], position[1]))

                if p1_within_x(position, x_min, x_max) and p1_within_y(position, y_min, y_max):
                    paths_that_hit.append((vel, copy(traced_path)))
                    break
                
                if vel_list[0] > 0:
                    vel_list[0] -= 1
                
                vel_list[1] -= 1
                
        print('##### Part 1 #####')
        print('Time', time() - t0)
        print('# of paths', len(paths_that_hit))

        if len(paths_that_hit) > 0:
            max_heigh_path = []
            max_height = 0
            for pth in paths_that_hit:
                x = pth[1]
                for coord in x:
                    if coord[1] > max_height:
                        max_height = coord[1]
                        max_heigh_path = x
            # print('Max Heigh Path', max_heigh_path)
            print('Max Height', max_height)


def part2():
    # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Answer: Just take the number of paths from part 1 #
    # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    with open(input_file_name) as f:
        lines = f.readlines()

part1()