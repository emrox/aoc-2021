import os
import re


# method taken and adopted from https://stackoverflow.com/a/62656964/1302662
def computeAllPossiblePaths(graph, currentVertex, visited):
    visited.append(currentVertex)
    is_big_cave_pattern = re.compile(r'[A-Z]+')

    for vertex in graph[currentVertex]:
        if vertex not in visited or is_big_cave_pattern.match(vertex) is not None:
            computeAllPossiblePaths(graph, vertex, visited.copy())

    allPossiblePaths.append(visited)


base_directory = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(base_directory, 'input')

lines = list(map(lambda l: l.split('-'), open(input_file, 'r').read().strip().split('\n')))
graph = {}

# build graph
for line in lines:
    if line[0] in graph:
        if line[1] not in graph[line[0]]:
            graph[line[0]].append(line[1])
    else:
        graph[line[0]] = [line[1]]

    if line[1] in graph:
        if line[0] not in line[1]:
            graph[line[1]].append(line[0])
    else:
        graph[line[1]] = [line[0]]


allPossiblePaths = []
computeAllPossiblePaths(graph, 'start', [])

validPathes = []
for possiblePath in allPossiblePaths:
    if possiblePath[-1] != 'end':
        continue

    validPathes.append(possiblePath)

print(len(validPathes))
