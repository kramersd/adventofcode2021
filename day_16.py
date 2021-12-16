from time import time

# input_file_name = 'aoc_puzzle16_input.txt'
input_file_name = 'day_16_sample.txt'

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

    children_packets = []

    parent_packet = None

    literal_value = 'NA'

    sub_bits = None

    def __init__(self, packet_type, packet_version):
        self.packet_type = packet_type
        self.packet_version = packet_version
    
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

    def add_child(self, packet):
        self.children_packets.append(packet)
    
    def get_children(self):
        return self.children_packets

    def get_sub_bits(self):
        return self.sub_bits
        

def get_packet(bin):
    packet_version = bin[:3]
    bin = bin[3:]

    packet_type = bin[:3]
    bin = bin[3:]

    # print('Version', int(packet_version, 2))
    # print('Type', int(packet_type, 2))

    if int(packet_type, 2) == 4:
        # print('Literal Packet')
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
        # print('Literal Value', int(s, 2))

        packet = Packet(packet_type, packet_version)
        packet.literal_value = int(s, 2)
        return (bin, packet)
    else:
        # print('Operator Packet')
        len_type_id = bin[:1]
        bin = bin[1:]

        if len_type_id == '0':
            # print('Len Type 0')
            packet = Packet(packet_type, packet_version)
            packet.num_bits = bin[:15]
            bin = bin[15:]
            packet.sub_bits = bin[:packet.get_num_bits()]
            # print('Sub bits', packet.get_sub_bits())
            bin = bin[packet.get_num_bits():]
            return (bin, packet)
        
        elif len_type_id == '1':
            # print('Len Type 1')
            packet = Packet(packet_type, packet_version)
            packet.num_children = bin[:11]
            bin = bin[11:]
            # print('Num Children', packet.get_num_children())

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
            print('Adding Child packet', packet)
            pp = parent_packets[len(parent_packets) - 1]
            print('Parent packet', pp)
            pp.add_child(packet)
            print('Children', pp.get_children())
            print('Children of children', packet.get_children())

            if len(pp.children_packets) == pp.get_num_children():
                # print('Removing parent')
                parent_packets.pop(len(parent_packets) - 1)
        
        if packet.get_num_children() > 0:
            print('Found a parent', packet.get_num_children())
            print('Parent XYZ', packet)
            parent_packets.append(packet)
            print('Parent packets', parent_packets)
        
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
        
        print('Hex Input', len(hex_input))
        print('Bin Input', len(bin_input))
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
        print('Packets', master_packet_list)
        print('---------------------------------------')

        versions = []
        for packet in master_packet_list:
            print(('Packet', packet))
            print('Children', len(packet.get_children()))
            versions.append(packet.get_packet_version())

        # print('Versions', versions)
        print('Total Sum of Versions', sum(versions))
        # print('Total Sum of Versions', sum(master_packet_list))

part1()
