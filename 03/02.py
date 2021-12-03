import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '03.input'

with open(os.path.join(base_directory, input_file)) as file:
    input_bits = [list(line.strip()) for line in file.readlines()]

bit_size = len(input_bits[0])
lines = len(input_bits)
oxygen_bits = input_bits
co2_bits = input_bits

def most_common_bit_in_position(bit_position, input_list):
    return str(int(len(list(filter(lambda bit: bit[bit_position] == '1', input_list))) * 2 > len(input_list)))

for bit_position in range(bit_size):
    if len(oxygen_bits) > 1:
        mcbip = most_common_bit_in_position(bit_position, oxygen_bits)
        oxygen_pre_filtered_counts = len(
            list(filter(lambda bits: bits[bit_position] == mcbip, oxygen_bits))
        )
        oxygen_filter_value = mcbip if oxygen_pre_filtered_counts * 2 != len(oxygen_bits) else '1'
        oxygen_bits = list(filter(lambda bits: bits[bit_position] == oxygen_filter_value, oxygen_bits))

    if len(co2_bits) > 1:
        mcbip = most_common_bit_in_position(bit_position, co2_bits)
        co2_pre_filtered_counts = len(
            list(filter(lambda bits: bits[bit_position] != mcbip, co2_bits))
        )
        co2_filter_value = mcbip if co2_pre_filtered_counts * 2 != len(co2_bits) else '1'
        co2_bits = list(filter(lambda bits: bits[bit_position] != co2_filter_value, co2_bits))

oxygen_rate = int(''.join(oxygen_bits[0]), 2)
co2_rate = int(''.join(co2_bits[0]), 2)

print(oxygen_rate * co2_rate)
