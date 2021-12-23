from dataclasses import dataclass
from typing import Generator


@dataclass
class Point:
    x: int
    y: int
    z: int

    def to_list(self):
        return [self.x, self.y, self.z]


@dataclass
class Shape:
    mode: str
    p1: Point
    p2: Point

    def __init__(self, mode, x, y, z: str):
        self.mode = mode

        x1, x2 = [int(a) for a in x.split('..')]
        y1, y2 = [int(a) for a in y.split('..')]
        z1, z2 = [int(a) for a in z.split('..')]

        self.p1 = Point(x1, y1, z1)
        self.p2 = Point(x2, y2, z2)

    def get_contained_points(self):
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                for z in range(self.p1.z, self.p2.z + 1):
                    yield Point(x, y, z)

    def verticies(self):
        p1 = self.p1
        p2 = Point(self.p2.x + 1, self.p2.y + 1, self.p2.z + 1)
        return [
            p1,
            Point(p2.x, p1.y, p1.x),
            Point(p2.x, p2.y, p1.x),
            Point(p1.x, p2.y, p1.x),
            Point(p1.x, p1.y, p2.x),
            Point(p2.x, p1.y, p2.x),
            p2,
            Point(p1.x, p2.y, p2.x),
        ]

    def openscad(self):
        shift = self.p1.to_list()
        ret_string = 'cube('
        ret_string += str(
            Point(
                self.p2.x + 1 - self.p1.x,
                self.p2.y + 1 - self.p1.y,
                self.p2.z + 1 - self.p1.z,
            ).to_list()
        )
        ret_string += ', center=false);'
        if shift[0] != 0 and shift[1] != 0 and shift[2] != 0:
            ret_string = 'translate(' + str(shift) + ') {\n' + ret_string + '\n};'
        return ret_string


def parse(input):
    commands = list()
    for line in input.strip().splitlines():
        value, coords = line.split(' ')
        x, y, z = [coord.split('=')[-1] for coord in coords.split(',')]
        commands.append(Shape(value, x, y, z))
    return commands


def q2():
    with open('day 22\sample.txt', 'r') as f:
        input = f.read()
    shapes = parse(input)

    current_program = shapes[0].openscad()
    for shape in shapes[1:]:
        mode = ''
        if shape.mode == 'on':
            mode = 'union'
        else:
            mode = 'difference'

        current_program = f'{mode}() {{\n{current_program}\n{shape.openscad()}\n}};'

    with open('day 22\openscad_output.scad', 'w') as f:
        f.write(current_program)

    print(current_program)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 2: {(pt2-st)*1000}ms')
