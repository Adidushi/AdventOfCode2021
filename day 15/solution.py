from heapq import heappop, heappush

def neighbors(matrix, r, c):
    for r, c in [(r+1, c), (r, c+1)]:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            yield (r, c)

def shortest_distance(t, data):
    heap = [(0, 0, 0)]
    seen = {(0, 0)}
    while heap:
        distance, x, y = heappop(heap)
        if x == t * len(data) - 1 and y == t * len(data[0]) - 1:
            return distance

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x_, y_ = x + dx, y + dy
            if x_ < 0 or y_ < 0 or x_ >= t * len(data) or y_ >= t * len(data):
                continue

            a, am = divmod(x_, len(data))
            b, bm = divmod(y_, len(data[0]))
            n = ((data[am][bm] + a + b) - 1) % 9 + 1

            if (x_, y_) not in seen:
                seen.add((x_, y_))
                heappush(heap, (distance + n, x_, y_))


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
