from os.path import sep

def calc_consumption(distance):
    return int(distance * (distance + 1) / 2)

def q1():
    with open(f'day 7{sep}input.txt', 'r') as f:
        input = list(map(int, f.read().strip().split(',')))

    return min([sum([abs(num - pos) for num in input]) for pos in range(min(input), max(input))])
    
def q2():
    with open(f'day 7{sep}input.txt', 'r') as f:
        input = list(map(int, f.read().strip().split(',')))

    return min([sum([calc_consumption(abs(num - pos)) for num in input]) for pos in range(min(input), max(input))])

if __name__ == '__main__':
    from time import perf_counter
    start_time = perf_counter()
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
    end_time = perf_counter()
    print(f'Time to run (s): {end_time - start_time}')