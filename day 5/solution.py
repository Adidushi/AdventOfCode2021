from dataclasses import dataclass
import numpy as np

@dataclass
class Point:
    x: int
    y: int

def line(pos1, pos2):
    x1, y1 = pos1.x, pos1.y
    x0, y0 = pos2.x, pos2.y
    deltax = x1-x0
    dxsign = int(abs(deltax)/deltax)
    deltay = y1-y0
    dysign = int(abs(deltay)/deltay)
    deltaerr = abs(deltay/deltax)
    error = 0
    y = y0
    for x in range(x0, x1, dxsign):
        yield Point(x, y)
        error = error + deltaerr
        while error >= 0.5:
            y += dysign
            error -= 1
    yield Point(x1, y1)

def parse_line(line):
    """Returns 2 Points
    """
    separated = line.split(' -> ')
    pos1, pos2 = separated[0].split(','), separated[1].split(',')

    pos1 = Point(int(pos1[0]), int(pos1[1]))
    pos2 = Point(int(pos2[0]), int(pos2[1]))

    return pos1, pos2


def get_occupied_straight_spaces(pos1, pos2):
    """Returns list of Points
    """
    spaces = list()

    if pos1.x == pos2.x:
        if pos1.y > pos2.y:
            pos1.y, pos2.y = pos2.y, pos1.y
        for i in range(pos1.y, pos2.y+1):
            spaces.append(Point(pos1.x, i))
    elif pos1.y == pos2.y:
        if pos1.x > pos2.x:
            pos1.x, pos2.x = pos2.x, pos1.x
        for i in range(pos1.x, pos2.x+1):
            spaces.append(Point(i, pos1.y))
        
    return spaces

def get_occupied_all_spaces(pos1, pos2):
    """Returns list of Points
    """
    spaces = list()

    if pos1.x == pos2.x:
        if pos1.y > pos2.y:
            pos1.y, pos2.y = pos2.y, pos1.y
        for i in range(pos1.y, pos2.y+1):
            spaces.append(Point(pos1.x, i))
    elif pos1.y == pos2.y:
        if pos1.x > pos2.x:
            pos1.x, pos2.x = pos2.x, pos1.x
        for i in range(pos1.x, pos2.x+1):
            spaces.append(Point(i, pos1.y))
    elif abs(pos1.x - pos2.x) == abs(pos1.y - pos2.y):
        spaces = line(pos1, pos2)
        
    return spaces

def add_occupied(spaces, matrix):
    for point in spaces:
        matrix[point.x, point.y] += 1

def q1():
    with open('day 5\input.txt', 'r') as f:
        input = f.readlines()

    counter_matrix = np.zeros((991, 991), dtype=int)

    for line in input:
        pos1, pos2 = parse_line(line)
        spaces = get_occupied_straight_spaces(pos1, pos2)
        add_occupied(spaces, counter_matrix)
    
    return (counter_matrix > 1).sum()
    
def q2():
    with open('day 5\input.txt', 'r') as f:
        input = f.readlines()

    counter_matrix = np.zeros((1000, 1000), dtype=int)

    for line in input:
        pos1, pos2 = parse_line(line)
        spaces = get_occupied_all_spaces(pos1, pos2)
        add_occupied(spaces, counter_matrix)
    
    return (counter_matrix > 1).sum()

def draw_q2():
    from PIL import Image, ImageDraw
    import random
    with open('day 5\input.txt', 'r') as f:
        input = f.readlines()
    im = Image.new('RGB', (1000, 1000), (0, 0, 0))
    sect = Image.new('RGB', (1000, 1000), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    draw_sect = ImageDraw.Draw(sect)

    counter_matrix = np.zeros((1000, 1000), dtype=int)
    for index, line in enumerate(input):
        print (index)
        pos1, pos2 = parse_line(line)
        
        if pos1.x == pos2.x or pos1.y == pos2.y or abs(pos1.x - pos2.x) == abs(pos1.y - pos2.y):
            draw.line((pos1.x, pos1.y, pos2.x, pos2.y), fill=(random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))

        spaces = get_occupied_all_spaces(pos1, pos2)
        add_occupied(spaces, counter_matrix)

        for pos in zip(*np.where(counter_matrix > 1)):
            x, y = pos
            val = counter_matrix[x][y]
            draw_sect.point((x, y), fill=(51 * val, 51 * val, 51 * val))

        imgs = [sect, im]
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        imgs_comb = Image.fromarray( imgs_comb)
        imgs_comb.save(f'day 5\comb\{index}.jpg')
    imgs_comb.show()

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
    draw_q2()