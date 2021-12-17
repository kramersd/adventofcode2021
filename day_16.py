from time import time

input_file_name = 'aoc_puzzle16_input.txt'
# input_file_name = 'day_16_sample.txt'

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

class Packet:
    packet_version = 0
    packet_type = 0

    num_children = None
    num_bits = None

    children_packets = None

    parent_packet = None

    literal_value = 'NA'

    sub_bits = None

    solved_value = None

    def __init__(self, packet_type, packet_version):
        self.packet_type = packet_type
        self.packet_version = packet_version
        self.children_packets = []
    
    def __str__(self):
        t0 = 't' + str(self.get_packet_type())
        v0 = 'v' + str(self.get_packet_version())
        nc = 'nc' + str(self.get_num_children())
        lv = 'lv' + str(self.get_literal_value())
        nb = 'nb' + str(self.get_num_bits())

        return str((t0, v0, nc, lv, nb))
    
    def __repr__(self):
        t0 = 't' + str(self.get_packet_type())
        v0 = 'v' + str(self.get_packet_version())
        nc = 'nc' + str(self.get_num_children())
        lv = 'lv' + str(self.get_literal_value())
        nb = 'nb' + str(self.get_num_bits())

        return str((t0, v0, nc, lv, nb))
    
    def get_packet_version(self):
        return int(self.packet_version, 2)
    
    def get_packet_type(self):
        return int(self.packet_type, 2)
    
    def get_num_bits(self):
        if self.num_bits:
            return int(self.num_bits, 2)
        return 0
    
    def get_literal_value(self):
        return self.literal_value

    def get_num_children(self):
        if self.num_children:
            return int(self.num_children, 2)
        return 0
    
    def set_num_children(self, num):
        self.num_children = bin(num)

    def add_child(self, packet):
        self.children_packets.append(packet)
    
    def add_multiple_children(self, packets):
        self.children_packets.extend(packets)
    
    def get_children(self):
        return self.children_packets

    def get_sub_bits(self):
        return self.sub_bits
    
    def solve(self):
        if self.solved_value != None:
            return self.solved_value

        if self.get_num_children() > 0:
            if self.packet_type == 4:
                print(4, 'Error - Self with children')
                return
            elif self.get_packet_type() == 0:
                if self.solved_value == None:
                    self.solved_value = 0
                for child in self.get_children():
                    self.solved_value += child.solve()
                return self.solved_value
            elif self.get_packet_type() == 1:
                if not self.solved_value:
                    self.solved_value = 1
                for child in self.get_children():
                    self.solved_value *= child.solve()
                return self.solved_value
            elif self.get_packet_type() == 2:
                min1 = self.get_children()[0].solve()
                for child in self.get_children():
                    s1 = child.solve()
                    if s1 < min1:
                        min1 = s1
                self.solved_value = min1
                return self.solved_value
            elif self.get_packet_type() == 3:
                max1 = self.get_children()[0].solve()
                for child in self.get_children():
                    s1 = child.solve()
                    if s1 > max1:
                        max1 = s1
                self.solved_value = max1
                return self.solved_value
            elif self.get_packet_type() == 5:
                children = self.get_children()
                for i in range(len(children)):
                    children[i] = children[i].solve()
                if children[0] > children[1]:
                    self.solved_value = 1
                else:
                    self.solved_value = 0
                return self.solved_value
            elif self.get_packet_type() == 6:
                children = self.get_children()
                for i in range(len(children)):
                    children[i] = children[i].solve()
                if children[0] < children[1]:
                    self.solved_value = 1
                else:
                    self.solved_value = 0
                return self.solved_value
            elif self.get_packet_type() == 7:
                children = self.get_children()
                top_children = []

                if len(children) == 2:
                    top_children = [children[0].solve(), children[1].solve()]
                else:
                    for i in range(len(children)):
                        if len(children[i].get_children()) > 0:
                            top_children.append(children[i].solve())
                            break

                    q = [children[0]]

                    total_num_of_first_children = 0
                    while len(q) > 0:
                        p_packet = q.pop(0)
                        total_num_of_first_children += p_packet.get_num_children()
                        q.extend(p_packet.get_children())
                
                    top_children.append(children[total_num_of_first_children + 1].solve())
                
                if top_children[0] == top_children[1]:
                    self.solved_value = 1
                    return self.solved_value
                else:
                    self.solved_value = 0
                    return self.solved_value
                
        print('Packet Type - LV', self.get_packet_type())
        self.solved_value = self.literal_value
        return self.solved_value

def get_packet(bin):
    packet_version = bin[:3]
    bin = bin[3:]

    packet_type = bin[:3]
    bin = bin[3:]

    if int(packet_type, 2) == 4:
        found_last_number = False
        bin_nums = []

        while found_last_number == False:
            temp_num = bin[:5]
            bin_nums.append(temp_num[1:])
            bin = bin[5:]
            if temp_num[0] == '0':
                found_last_number = True
            
        s = ''
        for bn in bin_nums:
            s += bn
        
        packet = Packet(packet_type, packet_version)
        packet.literal_value = int(s, 2)
        return (bin, packet)
    else:
        len_type_id = bin[:1]
        bin = bin[1:]

        if len_type_id == '0':
            packet = Packet(packet_type, packet_version)
            packet.num_bits = bin[:15]
            bin = bin[15:]
            packet.sub_bits = bin[:packet.get_num_bits()]
            bin = bin[packet.get_num_bits():]
            return (bin, packet)
        
        elif len_type_id == '1':
            packet = Packet(packet_type, packet_version)
            packet.num_children = bin[:11]
            bin = bin[11:]

            return (bin, packet)

def process_bin_input(bin_input):
    packet_list = []
    parent_packets = []
    q = []
    while bin_input != '' and int(bin_input, 2) > 0:
        gp = get_packet(bin_input)

        bin = gp[0]
        packet = gp[1]

        if packet.get_num_bits() > 0:
            q.append(packet)

        if len(parent_packets) > 0:
            last_parent_packet = parent_packets[len(parent_packets) - 1]
            last_parent_packet.add_child(packet)
            if len(last_parent_packet.children_packets) == last_parent_packet.get_num_children():
                parent_packets.pop(len(parent_packets) - 1)
        
        if packet.get_num_children() > 0: 
            parent_packets.append(packet)
        
        packet_list.append(packet)
        bin_input = bin
    return (packet_list, q)

def part1():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()

        hex_input = []
        bin_input = ''
        for l in lines:
            for i in l:
                hex_input.append(i)
                bin_input += hex_to_bin[i]
        
        print('# of Hex Input', len(hex_input))
        print('# of Bin Input', len(bin_input))
        master_packet_list = []
        q = []

        aa = process_bin_input(bin_input)
        master_packet_list.extend(aa[0])
        q.extend(aa[1])
        
        while len(q) > 0:
            curr_packet = q.pop(0)
            
            bb = process_bin_input(curr_packet.get_sub_bits())
            master_packet_list.extend(bb[0])
            q.extend(bb[1])


        print('##### Part 1 #####')
        print('Total lines', len(lines))
        print('Time', time() - t0)

        versions = []
        for packet in master_packet_list:
            versions.append(packet.get_packet_version())

        print('Total Sum of Versions', sum(versions))
       

def part2():
    with open(input_file_name) as f:
        t0 = time()
        lines = f.readlines()

        hex_input = []
        bin_input = ''
        for l in lines:
            for i in l:
                hex_input.append(i)
                bin_input += hex_to_bin[i]
        
        print('# of Hex Input', len(hex_input))
        print('# of Bin Input', len(bin_input))
        master_packet_list = []
        q = []

        aa = process_bin_input(bin_input)
        master_packet_list.extend(aa[0])
        q.extend(aa[1])
        
        while len(q) > 0:
            curr_packet = q.pop(0)
            
            bb = process_bin_input(curr_packet.get_sub_bits())
            master_packet_list.extend(bb[0])
            curr_packet.add_multiple_children(bb[0])
            curr_packet.set_num_children(len(bb[0]))
            q.extend(bb[1])

        print('##### Part 2 #####')
        print('Total lines', len(lines))
        print('Time', time() - t0)

        print('Solved', master_packet_list[0].solve())


part2()