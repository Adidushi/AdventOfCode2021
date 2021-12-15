from heapq import heappop, heappush

def neighbors(matrix, r, c):
    for r, c in [(r+1, c), (r, c+1)]:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            yield (r, c)

def shortest_distance(scale, matrix):
    heap = [(0, 0, 0)]
    visited = {(0, 0)}
    while heap:
        distance, r, c = heappop(heap)
        if r == scale * len(matrix) - 1 and c == scale * len(matrix[0]) - 1:
            return distance

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            n_r, n_c = r + dx, c + dy
            if n_r < 0 or n_c < 0 or n_r >= scale * len(matrix) or n_c >= scale * len(matrix):
                continue

            a, am = divmod(n_r, len(matrix))
            b, bm = divmod(n_c, len(matrix[0]))
            n = ((matrix[am][bm] + a + b) - 1) % 9 + 1

            if (n_r, n_c) not in visited:
                visited.add((n_r, n_c))
                heappush(heap, (distance + n, n_r, n_c))


def q1():
    with open('day 15\sample.txt', 'r') as f:
        input = f.read().splitlines()

    input = [[int(ch) for ch in line] for line in input]

    return shortest_distance(1, input)


def q2():
    with open('day 15\input.txt', 'r') as f:
        input = f.read().splitlines()

    input = [[int(ch) for ch in line] for line in input]

    return shortest_distance(5, input)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(
        f'Time for exection:\nPart 1: {(pt1-st)*1000}ms\nPart 2: {(pt2-pt1)*1000}ms\nTotal: {(pt2-st)*1000}ms')
