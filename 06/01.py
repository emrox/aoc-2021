import os

base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

initial_fishe_ages = list(map(int, open(input_file, 'r').read().strip().split(',')))
population = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
breeding_days = 256

for fish_age in initial_fishe_ages:
    population[fish_age] += 1

for day in range(breeding_days):
    new_population = {}

    for fishes_age in population.keys():
        new_fish_age = fishes_age - 1

        if fishes_age == 0:
            new_fish_age = 6
            new_population[8] = population[fishes_age]

        new_population[new_fish_age] = new_population.get(new_fish_age, 0) + population[fishes_age]

    population = new_population

print(sum(population.values()))
