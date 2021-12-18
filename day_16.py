from time import time
from uuid import uuid4

input_file_name = 'aoc_puzzle16_input.txt'
# input_file_name = 'sample_day_16.txt'

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
    id = None
    packet_type = None
    packet_version = None
    number_of_children = None
    number_of_bits = None
    subpacket_bits = None
    literal_value = None
    children = None
    solved_value = None


    def __init__(self, packet_type, packet_version):
        self.id = uuid4()
        self.packet_type = packet_type
        self.packet_version = packet_version
        self.children = []
    
    def __str__(self):
        v0 = 'v' + str(self.get_packet_version())
        t1 = 't' + str(self.get_packet_type())
        lv = 'lv' + str(self.get_literal_value())
        nc = 'nc' + str(self.get_number_of_children())
        nb = 'nb' + str(self.get_number_of_bits())

        return str((v0, t1, lv, nc, nb))
    
    def __repr__(self):
        v0 = 'v' + str(self.get_packet_version())
        t1 = 't' + str(self.get_packet_type())
        lv = 'lv' + str(self.get_literal_value())
        nc = 'nc' + str(self.get_number_of_children())
        nb = 'nb' + str(self.get_number_of_bits())

        return str((v0, t1, lv, nc, nb))

    def __eq__(self, other):
        if not type(other) == Packet:
            return False
        
        return self.id == other.id


    def set_literal_value(self, literal_value):
        self.literal_value = literal_value
    
    def get_literal_value(self):
        return self.literal_value
    
    def get_packet_version(self):
        return self.packet_version
    
    def get_packet_type(self):
        return self.packet_type

    def set_number_of_bits(self, number_of_bits):
        self.number_of_bits = number_of_bits
    
    def get_number_of_bits(self):
        if self.number_of_bits != None:
            return self.number_of_bits
        return 0
    
    def set_number_of_children(self, number_of_children):
        self.number_of_children = number_of_children
    
    def get_number_of_children(self):
        if self.number_of_children != None:
            return self.number_of_children
        elif len(self.get_children()) > 0:
            return len(self.get_children())
        return 0
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_children(self):
        return self.children
    
    def get_subpacket_bits(self):
        return self.subpacket_bits
    
    def set_subpacket_bits(self, subpacket_bits):
        self.subpacket_bits = subpacket_bits
    
    def solve(self):
        if self.solved_value != None:
            return self.solved_value

        if self.get_number_of_children() > 0:
            if self.packet_type == 4:
                print('Error - Literal with children')
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
                if len(children) > 2:
                    print('Error - Type 5', len(children))
                if children[0] > children[1]:
                    self.solved_value = 1
                else:
                    self.solved_value = 0
                return self.solved_value
            elif self.get_packet_type() == 6:
                children = self.get_children()
                for i in range(len(children)):
                    children[i] = children[i].solve()
                if len(children) > 2:
                    print('Error - Type 6', len(children))
                if children[0] < children[1]:
                    self.solved_value = 1
                else:
                    self.solved_value = 0
                return self.solved_value
            elif self.get_packet_type() == 7:
                children = self.get_children()
                
                if len(children) > 2:
                    print('Error - Type 7', len(children))

                if children[0].solve() == children[1].solve():
                    self.solved_value = 1
                    return self.solved_value
                else:
                    self.solved_value = 0
                    return self.solved_value

        self.solved_value = self.literal_value
        return self.solved_value

def slice_from(bin_input, start):
    return bin_input[start:]


def get_packet(bin_input):
    while len(bin_input) > 0 and int(bin_input, 2) > 0:
        packet_version = int(bin_input[0:3], 2)
        bin_input = slice_from(bin_input, 3)

        packet_type = int(bin_input[0:3], 2)
        bin_input = slice_from(bin_input, 3)

        packet = None

        if packet_type == 4:
            bin_nums = []
            found_end = False
            while not found_end:
                prefix = bin_input[0:1]
                bin_num = bin_input[1:5]
                bin_input = slice_from(bin_input, 5)
                if prefix == '0':
                    found_end = True
                bin_nums.append(bin_num)
            
            str_num = ''
            for bn in bin_nums:
                str_num += bn
            
            packet = Packet(packet_type, packet_version)
            packet.set_literal_value(int(str_num, 2))
            
            return (bin_input, packet)
        
        else:
            length_id = int(bin_input[0:1])
            bin_input = slice_from(bin_input, 1)

            if length_id == 0:
                number_of_bits = int(bin_input[0:15], 2)
                bin_input = slice_from(bin_input, 15)

                packet = Packet(packet_type, packet_version)
                packet.set_number_of_bits(number_of_bits)
                packet.set_subpacket_bits(bin_input[0:number_of_bits])
                bin_input = slice_from(bin_input, number_of_bits)

                return (bin_input, packet)
            elif length_id == 1:
                number_of_children = int(bin_input[0:11], 2)
                bin_input = slice_from(bin_input, 11)

                packet = Packet(packet_type, packet_version)
                packet.set_number_of_children(number_of_children)

                return (bin_input, packet)

def process_bin_input(bin_input, parent = None):
    master_packet = None
    parent_packets = []
    q = []
    while len(bin_input) > 0 and int(bin_input, 2) > 0:
        gp = get_packet(bin_input)

        bin_input = gp[0]
        packet = gp[1]

        if master_packet == None:
            master_packet = packet

        if len(parent_packets) > 0:
            curr_parent_packet = parent_packets[len(parent_packets) - 1]
            curr_parent_packet.add_child(packet)
            if len(curr_parent_packet.get_children()) == curr_parent_packet.get_number_of_children():
                parent_packets.pop(len(parent_packets) - 1)
        elif parent != None:
            parent.add_child(packet)
        
        if packet.get_number_of_children() > 0:
            parent_packets.append(packet)
        
        if packet.get_number_of_bits() > 0:
            q.append(packet)
    
    return (master_packet, q)

def part1and2():
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

        pbi = process_bin_input(bin_input)

        master_packet = pbi[0]
        q = pbi[1]

        while len(q) > 0:
            current_packet = q.pop()

            pbi_q = process_bin_input(current_packet.get_subpacket_bits(), parent = current_packet)

            pbi_q[0]
            q.extend(pbi_q[1])
        
        all_queue = [master_packet]
        total_versions = 0
        all_packets = []
        while len(all_queue) > 0:
            packet = all_queue.pop(0)
            all_packets.append(packet)
            total_versions += packet.get_packet_version()
            all_queue.extend(packet.get_children())
        
        print('Time', time() - t0)
        print('Total Versions', total_versions)
        # print('All Packets', all_packets)
        print('Solved', master_packet.solve())

part1and2()