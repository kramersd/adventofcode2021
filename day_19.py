from time import time

# input_file_name = 'aoc_puzzle19_input.txt'
input_file_name = 'sample_day_19.txt'

class Scanner:
    id = None
    scanner_position = None
    positions_seen = None

    def __init__(self, id):
        self.id = id
        self.positions_seen = []
    
    def __str__(self):
        id = 'id' + str(self.id)
        lps = 'lps' + str(len(self.positions_seen))

        s = (id, lps)
        return str(s)
    
    def __repr__(self):
        id = 'id' + str(self.id)
        lps = 'len_ps' + str(len(self.positions_seen))

        s = (id, lps)
        return str(s)
    
    
    def add_position(self, position):
        self.positions_seen.append(position)
    
    def get_positions(self):
        return self.positions_seen
    

def part1():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()

        all_scanners = []
        
        for l in lines:
            if '---' in l:
                parts = l.split(" ")
                scanner = Scanner(int(parts[2]))
                all_scanners.append(scanner)
            elif ',' in l:
                scanner = all_scanners[len(all_scanners) - 1]
                coord = l.split(',')
                new_position = (int(coord[0].strip()), int(coord[1].strip()), int(coord[2].strip()))
                scanner.add_position(new_position)

        print('##### Part 1 #####')
        print('Time', time() - t0)
        print('All Scanners', all_scanners)
        

part1()