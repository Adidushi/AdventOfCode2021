from math import prod


def neighbors(matrix, r, c):
    for r, c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            yield (r, c)


def q1():
    with open('day 9\input.txt', 'r') as f:
        f = f.read()
        matrix = [list(map(int, line)) for line in f.splitlines()]
    return sum(1 + matrix[r][c] for r in range(len(matrix))
               for c in range(len(matrix[0]))
               if all(matrix[r][c] < matrix[r1][c1] for r1, c1 in neighbors(matrix, r, c)))


def search(matrix, r, c, visited):
    stack = [(r, c)]
    visited.add((r, c))
    pts = 0
    while stack:
        r, c = stack.pop()
        pts += 1
        for r, c in neighbors(matrix, r, c):
            if matrix[r][c] != 9 and (r, c) not in visited:
                visited.add((r, c))
                stack.append((r, c))
    return pts


def q2():
    with open('day 9\input.txt', 'r') as f:
        f = f.read()
        matrix = [list(map(int, line)) for line in f.splitlines()]

    visited = set()

    basins = [search(matrix, r, c, visited) for r in range(len(matrix)) for c in range(
        len(matrix[0])) if (r, c) not in visited and matrix[r][c] != 9]
    return prod(sorted(basins)[-3:])


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
