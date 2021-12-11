def flashes_left(matrix, flashed):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] > 9 and (r, c) not in flashed:
                return True
    return False


def get_neighbors(matrix, flashed, r, c):
    neighbors = ((r-1, c-1), (r-1, c), (r-1, c+1),
                 (r, c-1), (r, c+1),
                 (r+1, c-1), (r+1, c), (r+1, c+1))
    for r, c in neighbors:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and (r, c) not in flashed:
            yield (r, c)


def flash(matrix, flashed, r, c):
    neighbors = get_neighbors(matrix, flashed, r, c)
    for n_r, n_c in neighbors:
        matrix[n_r][n_c] += 1

    flashed.append((r, c))


def flash_all(matrix, flashed):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] > 9 and ((r, c) not in flashed):
                flash(matrix, flashed, r, c)
                return 1


def do_step(matrix):
    flashed = list()
    flashed_count = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] += 1

    while flashes_left(matrix, flashed):
        flash_all(matrix, flashed)
        flashed_count += 1

    for r, c in flashed:
        matrix[r][c] = 0

    return flashed_count


def q1(steps):
    with open('day 11\input.txt', 'r') as f:
        input = f.read().splitlines()
    matrix = list(map(list, input))

    for r_num, r in enumerate(matrix):
        for c_num, c in enumerate(r):
            matrix[r_num][c_num] = int(c)

    total_flashes = 0

    for _ in range(steps):
        total_flashes += do_step((matrix))

    return total_flashes


def q2():
    with open('day 11\input.txt', 'r') as f:
        input = f.read().splitlines()
    matrix = list(map(list, input))

    for r_num, r in enumerate(matrix):
        for c_num, c in enumerate(r):
            matrix[r_num][c_num] = int(c)

    counter = 1

    while True:
        step_flashes = do_step((matrix))
        if step_flashes == 100:
            return counter
        counter += 1


if __name__ == '__main__':
    steps_1 = 100

    print(f'Part 1: {q1(steps_1)}')
    print(f'Part 2: {q2()}')
