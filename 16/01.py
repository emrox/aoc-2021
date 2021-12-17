import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')
input = open(input_file, 'r').read().strip()


def hexdec_to_binary(str: str):
    return bin(int(str, 16))[2:].zfill(len(str) * 4)


def binary_to_dec(str):
    if str == '':
        return 0
    return int(str, 2)


def decode_litereal(str):
    chunk_count = int(len(str) / 5)
    output = ''

    for step in range(chunk_count):
        start_pos = (5 * step)
        chunk = str[start_pos:start_pos + 5]

        output += chunk[1:]

        if chunk[0:1] == 0:
            break

    return binary_to_dec(output), len(output)


def parse_packet(packet: str):
    packet_version = binary_to_dec(packet[0:3])
    packet_type_id = binary_to_dec(packet[3:6])

    if packet_type_id == 4:
        # literal value

        output = ''
        unprocessed = packet[6:]

        while len(unprocessed) >= 5:
            first_bit = unprocessed[0:1]
            output += unprocessed[1:5]
            unprocessed = unprocessed[5:]

            if first_bit == '0':
                break

        return unprocessed, packet_version

    else:
        # operator

        length_type_id = packet[6:7]

        if length_type_id == '0':
            operator_length = 15
            unprocessed = packet[7:]

            unprocessed = unprocessed[operator_length:]

            while len(unprocessed) > 7:
                unprocessed, add_version = parse_packet(unprocessed + '')
                packet_version += add_version

            return unprocessed, packet_version
        else:
            operator_length = 11
            subpacket_count = binary_to_dec(packet[7:7 + operator_length])
            unprocessed = packet[7 + operator_length:]

            for cnt in range(subpacket_count):
                unprocessed, add_version = parse_packet(unprocessed + '')
                packet_version += add_version

            return unprocessed, packet_version


binary = hexdec_to_binary(input)
_, version_sum = parse_packet(binary)
print(version_sum)
