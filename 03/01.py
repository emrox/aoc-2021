import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = '03.debug'

with open(os.path.join(base_directory, input_file)) as file:
    input_bits = [list(line.strip()) for line in file.readlines()]

bit_size = len(input_bits[0])
gamma_values = ''
epsilon_values = ''

for bit_position in range(bit_size):
    bit_val_counts = [0, 0]

    for bits in input_bits:
        bit = int(bits[bit_position])

        bit_val_counts[bit] += 1

    gamma_values += '0' if bit_val_counts[0] > bit_val_counts[1] else '1'
    epsilon_values += '1' if bit_val_counts[0] > bit_val_counts[1] else '0'

gamma_rate = int(gamma_values, 2)
epsilon_rate = int(epsilon_values, 2)

print(gamma_rate * epsilon_rate)
