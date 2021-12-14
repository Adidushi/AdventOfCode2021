def q1():
    with open('day \input.txt', 'r') as f:
        input = f.read().splitlines()
    
def q2():
    with open('day \input.txt', 'r') as f:
        input = f.read().splitlines()

if __name__ == '__main__':
    from time import perf_counter as  pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for exection:\nPart 1: {(pt1-st)*1000}ms\nPart 1: {(pt2-pt1)*1000}ms\nTotal: {(pt2-st)*1000}ms')