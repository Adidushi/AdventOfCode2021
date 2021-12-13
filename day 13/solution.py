def flip_x(dots, line):
    to_change = set()
    for c, r in dots:
        if c > line:
            to_change.add((c, r))

    for c, r in to_change:
        new_c = 2 * line - c
        dots.remove((c, r))
        dots.add((new_c, r))

def flip_y(dots, line):
    to_change = set()
    for c, r in dots:
        if r > line:
            to_change.add((c, r))

    for c, r in to_change:
        new_r = 2 * line - r
        dots.remove((c, r))
        dots.add((c, new_r))

def q1():
    with open('day 13\input.txt', 'r') as f:
        input = f.read()

    dots, folds = input.split('\n\n')
    
    dots = [pos.split(',') for pos in dots.splitlines()]
    folds = [cmd.split()[-1].split('=') for cmd in folds.splitlines()]
    
    dots = set((int(c), int(r)) for c, r in dots)

    dir, line = folds[0]

    line = int(line)
    if dir == 'x':
        flip_x(dots, line)
    elif dir == 'y':
        flip_y(dots, line)
    return len(dots)


    
def q2():
    with open('day 13\input.txt', 'r') as f:
        input = f.read()

    dots, folds = input.split('\n\n')
    
    dots = [pos.split(',') for pos in dots.splitlines()]
    folds = [cmd.split()[-1].split('=') for cmd in folds.splitlines()]
    
    dots = set((int(c), int(r)) for c, r in dots)

    for dir, line in folds:
        line = int(line)
        if dir == 'x':
            flip_x(dots, line)
        elif dir == 'y':
            flip_y(dots, line)

    ret_str = '\n'

    for r in range(6):
        for c in range(40):
            if (c, r) in dots:
                ret_str += '█'
            else:
                ret_str += ' '
        ret_str += '\n'

    return ret_str

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')