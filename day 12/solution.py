from collections import defaultdict


def paths(current, seen, touching_caves):
    if current == 'end':
        return 1
    if current.islower() and current in seen:
        return 0
    seen = seen | {current}
    return sum(paths(thing, seen, touching_caves) for thing in touching_caves[current])


def paths_mod(current: str, seen, duplicate, touching_caves):
    if current == 'end':
        return 1
    if current == "start" and seen:
        return 0
    if current.islower() and current in seen:
        if duplicate is None:
            duplicate = current
        else:
            return 0
    seen = seen | {current}
    return sum(paths_mod(thing, seen, duplicate, touching_caves) for thing in touching_caves[current])


def q1():
    with open('day 12\input.txt', 'r') as f:
        input = f.read().splitlines()

    touching_caves = defaultdict(list)
    for line in input:
        cave_1, cave_2 = line.split("-")
        touching_caves[cave_1].append(cave_2)
        touching_caves[cave_2].append(cave_1)

    return paths('start', set(), touching_caves)


def q2():
    with open('day 12\input.txt', 'r') as f:
        input = f.read().splitlines()

    touching_caves = defaultdict(list)
    for line in input:
        cave_1, cave_2 = line.split("-")
        touching_caves[cave_1].append(cave_2)
        touching_caves[cave_2].append(cave_1)

    return paths_mod('start', set(), None, touching_caves)


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
