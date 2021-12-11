import sys
sys.setrecursionlimit(1000)

def get_neighbors(matrix, flashed, r, c):
    neighbors = ((r-1, c-1), (r-1, c), (r-1, c+1),
                 (r, c-1), (r, c+1),
                 (r+1, c-1), (r+1, c), (r+1, c+1))
    for r, c in neighbors:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] not in flashed:
            yield (r, c)


def keep_flashing(matrix):
    for r_num, r in enumerate(matrix):
        for c_num, c in enumerate(r):
            if c > 9 and (r_num, c_num):
                return True
    return False


def flash(matrix, flashed, r, c):
    matrix[r][c] = 0
    flashed.add((r, c))
    for n_r, n_c in get_neighbors(matrix, flashed, r, c):
        if matrix[n_r][n_c] > 9:
            flash(matrix, flashed, r, c)


def do_step(matrix):
    print('new step!')
    flashed = set()

    # Add 1 to all octis
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c] += 1

    flash_total = 0

    to_add = set()

    while keep_flashing(matrix):
        for r, c in to_add:
            matrix[r][c] += 1
        to_add = set()
        for r in range(len(matrix)):
            for c in range(r):
                if matrix[r][c] > 9 and matrix[r][c] not in flashed:
                    flash(matrix, flashed, r, c)
                    # matrix[r][c] = 0
                    # flash_total += 1
                    # for n_r, n_c in get_neighbors(matrix, flashed, r, c):
                    #     matrix[n_r][n_c] += 1

    return flash_total


def q1(steps):
    with open('day 11\input.txt', 'r') as f:
        input = f.read().splitlines()
    matrix = list(map(list, input))
    for r_num, r in enumerate(matrix):
        for c_num, c in enumerate(r):
            matrix[r_num][c_num] = int(c)
    total = sum([do_step(matrix) for _ in range(steps)])
    return total


def q2():
    with open('day 11\input.txt', 'r') as f:
        input = f.read().splitlines()


if __name__ == '__main__':
    steps_1 = 100

    print(f'Part 1: {q1(steps_1)}')
    print(f'Part 2: {q2()}')
