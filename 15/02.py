import os


def numbers_to_int(line):
    return list(map(int, line))


base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')
base_cavemap = list(map(numbers_to_int, open(input_file, 'r').read().strip().split('\n')))

cavemap = []

for expand_y in range(5):
    for y, row in enumerate(base_cavemap):
        cavemap.append([])

        for expand_x in range(5):
            for x, col in enumerate(base_cavemap[y]):
                new_danger_level = base_cavemap[y][x] + expand_x + expand_y

                if new_danger_level >= 10:
                    new_danger_level -= 9

                cavemap[-1].append(new_danger_level)

nodes = ()
distances = {}

for y, row in enumerate(cavemap):
    for x, col in enumerate(row):
        point_name = f'{x}-{y}'

        nodes = (*list(nodes), point_name)

        if point_name not in distances:
            distances[point_name] = {}

        if x > 0:
            distances[point_name].update({f'{x - 1}-{y}': cavemap[y][x - 1]})

        if x < len(cavemap[0]) - 1:
            distances[point_name].update({f'{x + 1}-{y}': cavemap[y][x + 1]})

        if y > 0:
            distances[point_name].update({f'{x}-{y - 1}': cavemap[y - 1][x]})

        if y < len(cavemap) - 1:
            distances[point_name].update({f'{x}-{y + 1}': cavemap[y + 1][x]})

# Dijkstra's algorithm taken from https://stackoverflow.com/a/22899400/1302662
unvisited = {node: None for node in nodes}  # using None as +inf
visited = {}
current = '0-0'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
            continue

        newDistance = currentDistance + distance

        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance

    visited[current] = currentDistance

    del unvisited[current]

    if not unvisited:
        break

    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited[f'{len(cavemap[0]) - 1}-{len(cavemap) - 1}'])
