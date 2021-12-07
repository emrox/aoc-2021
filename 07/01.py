import os
import statistics

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

crab_positions = list(map(int, open(input_file, 'r').read().strip().split(',')))
median = int(statistics.median(crab_positions))

needed_fuel = 0

for crab_position in crab_positions:
    needed_fuel += abs(crab_position - median)

print(needed_fuel)
