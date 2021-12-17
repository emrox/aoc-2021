import os
import math

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')
input = open(input_file, 'r').read().strip()


def hexdec_to_binary(str: str):
    return bin(int(str, 16))[2:].zfill(len(str) * 4)


def binary_to_dec(str):
    if str == '':
        return 0
    return int(str, 2)


def parse_packet(packet: str, depth: int = 1):
    packet_version = binary_to_dec(packet[0:3])
    packet_type_id = binary_to_dec(packet[3:6])

    if packet.find('1') == -1:
        return '', 0, packet_version

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

        return unprocessed, binary_to_dec(output), packet_version + 0

    else:
        # operator

        length_type_id = packet[6:7]
        operator_length = 15 if length_type_id == '0' else 11
        unprocessed = packet[7 + operator_length:]
        process_values = []

        if length_type_id == '0':
            unprocessed = packet[7:]

            packet_length = binary_to_dec(unprocessed[:operator_length])
            unprocessed = unprocessed[operator_length:]

            packet_unprocessed = unprocessed[:packet_length]
            unprocessed = unprocessed[packet_length:]

            while len(packet_unprocessed) > 7:
                packet_unprocessed, process_result, add_version = parse_packet(packet_unprocessed + '', depth + 1)
                packet_version += add_version
                process_values.append(process_result)

        else:
            subpacket_count = binary_to_dec(packet[7:7 + operator_length])

            for _ in range(subpacket_count):
                unprocessed, process_result, add_version = parse_packet(unprocessed + '', depth + 1)
                packet_version += add_version
                process_values.append(process_result)

        result = 0

        if packet_type_id == 0:
            result = sum(process_values)
        elif packet_type_id == 1:
            result = math.prod(process_values)
        elif packet_type_id == 2:
            result = sorted(process_values)[0]
        elif packet_type_id == 3:
            result = sorted(process_values)[-1]
        elif packet_type_id == 5:
            result = 1 if process_values[0] > process_values[1] else 0
        elif packet_type_id == 6:
            result = 1 if process_values[0] < process_values[1] else 0
        elif packet_type_id == 7:
            result = 1 if process_values[0] == process_values[1] else 0

        return unprocessed, result, packet_version + 0


binary = hexdec_to_binary(input)
rest, result, version_sum = parse_packet(binary)

print(f'result: {result} version: {version_sum}')
