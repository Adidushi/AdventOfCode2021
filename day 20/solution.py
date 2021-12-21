def parse(raw_input):
    enhancement = raw_input[0].replace('.', '0').replace('#', '1')

    image = [f'.{line}.' for line in raw_input[2:]]
    blank_line = '.' * len(image[1])
    image.insert(0, blank_line)
    image.append(blank_line)

    for index in range(len(image)):
        image[index] = list(image[index].replace('.', '0').replace('#', '1'))

    return enhancement, list(image)


def get_value(input, r, c, iteration):
    if iteration % 2 == 1:
        new_char = '1'
    else:
        new_char = '0'

    value = ''
    for n_r in range(r-1, r+2):
        for n_c in range(c-1, c+2):
            try:
                value += input[n_r][n_c]
            except IndexError:
                value += new_char

    return int(value, 2)


def translate_value(enhancement, value):
    return enhancement[value]


def print_image(image):
    for line in image:
        print(line.replace('1', '█').replace('0', '.'))


def pad_image(image, iteration):
    if iteration % 2 == 1:
        new_char = list('1')
    else:
        new_char = list('0')
    image = [new_char + list(line) + new_char for line in image]
    image.insert(0, '')
    image.append('')
    return image


def q1(iterations):
    with open('day 20\input.txt', 'r') as f:
        input = f.read().splitlines()
    enhancement, image = parse(input)
    for iteration in range(iterations):
        new_image = list()
        image = pad_image(image, iteration)
        for r in range(len(image)):
            line = ''
            for c in range(len(image[1])):
                value = get_value(image, r, c, iteration)
                line += enhancement[value]
            new_image.append(line)
        image = new_image

    return ''.join(image).count('1')


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1(2)}')
    pt1 = pc()
    print(f'Part 2: {q1(50)}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
