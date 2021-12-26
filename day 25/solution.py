from copy import deepcopy

def which_can_move_east(seabed):
    movables = set()
    for row in range(len(seabed)):
        for col in range(len(seabed[0])):
            try:
                if seabed[row][col] == '>' and seabed[row][col + 1] == '.':
                    movables.add((row, col))
            except IndexError:
                if seabed[row][col] == '>' and seabed[row][0] == '.':
                    movables.add((row, col))
    return movables

def move_east(seabed, movables):
    for row, col in movables:
        seabed[row][col] = '.'
        try:
            seabed[row][col + 1] = '>'
        except IndexError:
            seabed[row][0] = '>'

def which_can_move_south(seabed):
    movables = set()
    for row in range(len(seabed)):
        for col in range(len(seabed[0])):
            try:
                if seabed[row][col] == 'v' and seabed[row + 1][col] == '.':
                    movables.add((row, col))
            except IndexError:
                if seabed[row][col] == 'v' and seabed[0][col] == '.':
                    movables.add((row, col))
    return movables

def move_south(seabed, movables):
    for row, col in movables:
        seabed[row][col] = '.'
        try:
            seabed[row + 1][col] = 'v'
        except IndexError:
            seabed[0][col] = 'v'

def migrate(input):
    east_movables = which_can_move_east(input)
    move_east(input, east_movables)

    south_movables = which_can_move_south(input)
    move_south(input, south_movables)

    if not east_movables and not south_movables:
        return True
    
    return False


def print_seabed(seabed):
    for line in seabed:
        print(''.join(line))


def q1():
    with open('day 25\input.txt', 'r') as f:
        input = f.read().splitlines()
    input = [list(line) for line in input]

    same = False
    counter = 0
    while not same:
        same = migrate(input)
        counter += 1
    return counter

    

    
    
    
def q2():
    with open('day 25\input.txt', 'r') as f:
        input = f.read().splitlines()

if __name__ == '__main__':
    from time import perf_counter as  pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')