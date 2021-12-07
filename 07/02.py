import os
import statistics
from math import ceil, floor

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

crab_positions = list(map(int, open(input_file, 'r').read().strip().split(',')))
mean = floor(statistics.mean(crab_positions))

needed_fuel = 0

for crab_position in crab_positions:
    distance = abs(crab_position - mean)
    needed_fuel += sum(range(distance + 1))

print(needed_fuel)
