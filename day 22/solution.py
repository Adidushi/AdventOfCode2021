import itertools
from dataclasses import dataclass
from math import prod

def contains_all(big_cube, small_cube) -> bool:
    pass

def intersects(cube_1, cube_2) -> bool:
    for coord in cube_2.x:
        if cube_1.x[0] <= coord <= cube_1.x[1]: return True
    for coord in cube_2.y:
        if cube_1.y[0] <= coord <= cube_1.y[1]: return True
    for coord in cube_2.z:
        if cube_1.z[0] <= coord <= cube_1.z[1]: return True
    return False


@dataclass
class Cube:
    x: tuple(int, int)
    y: tuple(int, int)
    z: tuple(int, int)

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash(str(self))

    def get_size(self):
        diffs = map(lambda c: abs(c[0] - c[1]), (self.x, self.y, self.z))
        return prod(diffs)

    def intersects(self, other):
        for coord in other.x:
            if self.x[0] <= coord <= self.x[1]: return True
        for coord in other.y:
            if self.y[0] <= coord <= self.y[1]: return True
        for coord in other.z:
            if self.z[0] <= coord <= self.z[1]: return True
        return False
    
    def split(self, other):
        pass

        


def create_matrix() -> dict:
    cube_matrix = dict()
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                cube_matrix[(x, y, z)] = False
    return cube_matrix

def parse_input_q1(input):

    command_list = list()

    for command in input:
        value, coords = command.split(' ')
        if value == 'on':
            value = True
        elif value == 'off':
            value = False
        coords = list(
            map(lambda coord: coord[2:].split('..'), coords.split(',')))
        ranges = list()
        for coord in coords:
            ranges.append(
                range(max(int(coord[0]), -50), min(51, int(coord[1]) + 1)))
        x, y, z = ranges

        command_list.append({'value': value, 'x': x, 'y': y, 'z': z})
    return command_list


def q1():
    with open('day 22\input.txt', 'r') as f:
        input = f.read().splitlines()

    cube_matrix = set()
    commands = parse_input_q1(input)
    for command in commands:
        for coord in itertools.product(command['x'], command['y'], command['z']):
            cube_matrix.add(coord) if command['value'] else cube_matrix.discard(coord)

    return len(cube_matrix)


def parse_input_q2(input):

    command_list = list()

    for command in input:
        value, coords = command.split(' ')
        if value == 'on':
            value = True
        elif value == 'off':
            value = False
        coords = list(
            map(lambda coord: coord[2:].split('..'), coords.split(',')))
        ranges = list()
        for coord in coords:
            ranges.append(
                range(int(coord[0]), int(coord[1]) + 1))
        x, y, z = ranges

        command_list.append({'value': value, 'x': x, 'y': y, 'z': z})
    return command_list


def q2():
    with open('day 22\sample.txt', 'r') as f:
        input = f.read().splitlines()

    cube_matrix = set()

    commands = parse_input_q2(input)
    counter = 0
    for command in commands:
        counter += 1
        print(counter)
        for coord in itertools.product(command['x'], command['y'], command['z']):
            cube_matrix.add(coord) if command['value'] else cube_matrix.discard(coord)

    return len(cube_matrix)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
