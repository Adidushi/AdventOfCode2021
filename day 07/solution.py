def q1():
    with open('day 07\input.txt', 'r') as f:
        input = f.read()
        # input = list(map(int, input.strip().split(',')))

    return min([sum([abs(num - pos) for num in list(map(int, input.strip().split(',')))]) for pos in range(min(list(map(int, input.strip().split(',')))), max(list(map(int, input.strip().split(',')))))])


def q2():
    with open('day 07\input.txt', 'r') as f:
        input = f.read()
        # input = list(map(int, f.read().strip().split(',')))

    return min([sum([int(abs(num - pos) * (abs(num - pos) + 1) / 2) for num in list(map(int, input.strip().split(',')))]) for pos in range(min(list(map(int, input.strip().split(',')))), max(list(map(int, input.strip().split(',')))))])


if __name__ == '__main__':
    from time import perf_counter
    start_time = perf_counter()
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
    end_time = perf_counter()
    print(f'Time to run (s): {end_time - start_time}')
