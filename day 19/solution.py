from itertools import permutations, product
import numpy as np

AXES = [np.array(perm) for perm in permutations([1, 2, 3])]
DIRS = [np.array(prod) for prod in product([-1, 1], [-1, 1], [-1, 1])]
ALL_PERMS = [(axis, direction) for axis, direction in product(AXES, DIRS)]


class Scanner:
    def __init__(self, points: str, index):
        lines = points.splitlines()
        self.points = np.array([[int(x) for x in l.split(',')]
                               for l in lines[1:]], dtype='int16')
        self.pos = None
        self.index = index

    def find_offset(self, other: 'Scanner'):
        if other.pos is not None:
            return False
        my_points_cp = self.points
        for ax, d in ALL_PERMS:
            other_points_cp = other.points[:, ax - 1] * d
            d = my_points_cp[np.newaxis, :] - other_points_cp[:, np.newaxis]
            uniques = [np.unique(d[..., i], return_counts=True)
                       for i in range(3)]

            if all([max(unique[1]) >= 12 for unique in uniques]):

                other.points = other_points_cp
                other.pos = np.array([unique[0][unique[1] >= 12][0]
                                     for unique in uniques], dtype='int16') + self.pos

                # print(f'found {other.index}: {other.pos}')
                return True

        return False


def q1():
    with open('day 19\sample.txt', 'r') as f:
        input = f.read().split('\n\n')

    scanners = [Scanner(block, index) for index, block in enumerate(input)]
    scanners[0].pos = np.array([0, 0, 0])

    while any(s.pos is None for s in scanners):
        for unknown in filter(lambda x: x.pos is None, scanners):
            for known in scanners:
                if known.pos is not None and known.find_offset(unknown):
                    break

    beacons = set()
    for scanner in scanners:
        for point in (scanner.points + scanner.pos):
            beacons.add(tuple(point))
    return len(beacons), scanners


def q2(scanners):
    farthest = 0
    for scanner_1 in scanners:
        for scanner_2 in scanners:
            if scanner_1 is not scanner_2:
                distance = np.abs(scanner_1.pos - scanner_2.pos).sum()
                farthest = max(farthest, distance)
    return farthest


def visualize(scanners):
    import plotly.express as px
    import pandas as pd

    data = list()
    for scanner in scanners:
        for point in (scanner.points + scanner.pos):
            data.append((*point, 'Beacon', 0))
        data.append((*scanner.pos, 'Scanner', scanner.index))
    data.append((0, 0, 0, 'Origin', 0))

    data = pd.DataFrame(data, columns=['x', 'y', 'z', 'type', 'index'])
    fig = px.scatter_3d(data, x='x', y='y', z='z', color='type', symbol='type')
    fig.show()


if __name__ == '__main__':
    from time import perf_counter as pc

    st = pc()
    ans, scanners = q1()
    print(f'Part 1: {ans}')
    pt1 = pc()
    print(f'Part 2: {q2(scanners)}')
    pt2 = pc()

    if input("Visualize?"):
        visualize(scanners)

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
