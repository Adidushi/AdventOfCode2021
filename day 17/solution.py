x = (56, 76)
y = (-162, -134)
min_x, max_x = x
min_y, max_y = y


def do_y_step(y_pos, y_velocity):
    y_pos += y_velocity
    y_velocity -= 1
    return y_pos, y_velocity


def check_y(y_velocity):
    y_pos = 0
    highest_y = 0
    while y_pos >= max_y:
        y_pos, y_velocity = do_y_step(y_pos, y_velocity)
        if y_pos > highest_y:
            highest_y = y_pos
    return (y_pos >= min_y), highest_y


def find_y_value():
    best_y = 0
    top_value = 0
    highest_check = abs(max_y * 3)
    for y_to_check in range(highest_check):
        valid_y, highest_val = check_y(y_to_check)
        if valid_y:
            best_y = y_to_check
            top_value = highest_val
    return best_y, top_value


def check_y_steps(y_velocity):
    y_pos = 0
    steps = 0
    while y_pos > max_y:
        y_pos, y_velocity = do_y_step(y_pos, y_velocity)
        steps += 1
    return (min_y <= y_pos <= max_y), steps


def check_x_position(x_velocity, steps):
    x_pos = 0
    for i in range(steps):
        x_pos += x_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
    return min_x <= x_pos <= max_x


def q1():
    best_y, top_value = find_y_value()
    return best_y, top_value


def q2():
    highest_y = find_y_value()[0] + 1
    lowest_y = min_y
    counter = 0

    for y_velocity in range(lowest_y, highest_y):
        valid, steps = check_y_steps(y_velocity)
        if valid:
            for x_velocity in range(max_x + 1):
                if check_x_position(x_velocity, steps):
                    counter += 1

    return counter + 1



if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
