import math
import json


class SnailNumber:
    def __init__(self, left, right, depth=0, parent=None):

        if isinstance(left, list):
            self.left = SnailNumber(left[0], left[1], depth+1, self)
        else:
            self.left = left

        if isinstance(right, list):
            self.right = SnailNumber(right[0], right[1], depth+1, self)
        else:
            self.right = right

        self.depth = depth
        self.parent = parent

    def ls_idx(self):
        ret_list = list()

        if isinstance(self.left, int):
            ret_list.append((self.left, self.depth))
        else:
            ret_list.extend(self.left.ls_idx())
        if isinstance(self.right, int):
            ret_list.append((self.right, self.depth))
        else:
            ret_list.extend(self.right.ls_idx())
        return ret_list


def add_list(first, second):
    summed = list()
    for element in first+second:
        summed.append((element[0], element[1]+1))
    return summed


def sum_once(node_list, level_to_sum):
    for index, element in enumerate(node_list):
        if element[1] == level_to_sum:
            node_list[index] = (node_list[index][0] * 3 + 2 *
                                node_list[index + 1][0], node_list[index][1] - 1)
            node_list.pop(index + 1)
            return node_list, True

    return node_list, False


def magnitude(node_list):
    for level in (3, 2, 1):
        acted = True
        while acted:
            node_list, acted = sum_once(node_list, level)
    return node_list[0][0] * 3 + 2 * node_list[1][0]


def explode(node_list):
    for index, value in enumerate(node_list):
        value, depth = value
        if depth == 4:
            if index > 0:
                node_list[index - 1] = (node_list[index - 1]
                                        [0] + value, node_list[index - 1][1])
            if index + 2 < len(node_list):
                node_list[index + 2] = (node_list[index + 2][0] +
                                        node_list[index + 1][0], node_list[index + 2][1])

            node_list[index] = (0, 3)

            if index + 1 < len(node_list):
                node_list.pop(index + 1)

            return node_list, True
    return node_list, False


def split(node_list):
    for index, value in enumerate(node_list):
        value, depth = value
        if value >= 10:
            new_list = node_list[:index] + [(math.floor(value / 2), depth + 1), (math.ceil(
                value / 2), depth + 1)] + node_list[index + 1:]
            return new_list, True
    return node_list, False


def reduce(node_list):
    while True:
        node_list, acted = explode(node_list)
        if acted:
            continue

        node_list, acted = split(node_list)
        if acted:
            continue

        break
    return node_list


def q1():
    with open('day 18\input.txt', 'r') as f:
        input = f.read().splitlines()

    snail_list = list()

    for line in input:
        snail_list.append(SnailNumber(*json.loads(line)).ls_idx())

    current_list = snail_list.pop(0)
    while snail_list:
        current_list = add_list(current_list, snail_list.pop(0))
        current_list = reduce(current_list)

    return magnitude(current_list)


def q2():
    with open('day 18\input.txt', 'r') as f:
        input = f.read().splitlines()

    snail_list = list()

    for line in input:
        snail_list.append(SnailNumber(*json.loads(line)).ls_idx())

    max_mag = 0
    for index, first_num in enumerate(snail_list):
        current_list = snail_list.copy()
        current_list.pop(index)
        for second_num in current_list:
            num_to_check = reduce(add_list(first_num, second_num))
            max_mag = max(magnitude(num_to_check), max_mag)

    return max_mag


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
