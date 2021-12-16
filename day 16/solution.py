from math import prod

binary_string = ''


class Packet:
    def __init__(self, version, packet_type, value, subpackets):
        self.version = version
        self.packet_type = packet_type
        self.value = value
        self.subpackets = subpackets

    def check_sum(self):
        return self.version + sum(packet.check_sum() for packet in self.subpackets)

    def eval(self):
        match self.packet_type:
            case 0: return sum(subpacket.eval() for subpacket in self.subpackets)
            case 1: return prod(subpacket.eval() for subpacket in self.subpackets)
            case 2: return min(subpacket.eval() for subpacket in self.subpackets)
            case 3: return max(subpacket.eval() for subpacket in self.subpackets)
            case 4: return self.value
            case 5: return self.subpackets[0].eval() > self.subpackets[1].eval()
            case 6: return self.subpackets[0].eval() < self.subpackets[1].eval()
            case 7: return self.subpackets[0].eval() == self.subpackets[1].eval()


def read_bits(n):
    global binary_string

    return_value = ""
    if n > 0:
        return_value, binary_string = binary_string[:n], binary_string[n:]
    else:
        while binary_string[0] == "1":
            return_value, binary_string = return_value + \
                binary_string[1:5], binary_string[5:]
        return_value, binary_string = return_value + \
            binary_string[1:5], binary_string[5:]

    return int(return_value, 2)


def parse():
    version = read_bits(3)
    packet_type = read_bits(3)
    value = None
    subpackets = []

    if packet_type == 4:
        value = read_bits(-1)
    else:
        lid = read_bits(1)
        if lid == 0:
            size = read_bits(15)
            length = len(binary_string)
            while length - len(binary_string) != size:
                subpackets.append(parse())
        else:
            count = read_bits(11)
            for _ in range(count):
                subpackets.append(parse())

    return Packet(version=version, packet_type=packet_type, value=value, subpackets=subpackets)


def q1():
    global binary_string

    with open('day 16\input.txt', 'r') as f:
        input = f.read().strip()

    binary_string = bin(int(input, 16))[2:].zfill(
        4 - len(bin(int(input, 16))[2:]) % 4 + len(bin(int(input, 16))[2:]))

    return parse().check_sum()


def q2():
    global binary_string
    with open('day 16\input.txt', 'r') as f:
        input = f.read().strip()

    binary_string = bin(int(input, 16))[2:].zfill(
        4 - len(bin(int(input, 16))[2:]) % 4 + len(bin(int(input, 16))[2:]))

    return parse().eval()


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n'
          f'Part 1: {(pt1-st)*1000}ms\n'
          f'Part 2: {(pt2-pt1)*1000}ms\n'
          f'Total: {(pt2-st)*1000}ms')
