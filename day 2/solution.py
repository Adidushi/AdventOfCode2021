def q1():
    with open('day 2\input.txt', 'r') as f:
        input = f.readlines()

    h_pos = 0
    v_pos = 0

    for line in input:
        action, amount = line.split()
        amount = int(amount)

        if action == 'forward':
            h_pos += amount
        elif action == 'up':
            v_pos -= amount
        elif action == 'down':
            v_pos += amount

    print(f'Final positions:\nVertical: {v_pos}\nHorizontal: {h_pos}')
    print(f'Final answer: {h_pos * v_pos}')


def q2():
    with open('day 2\input.txt', 'r') as f:
        input = f.readlines()

    h_pos = 0
    v_pos = 0
    aim = 0

    for line in input:
        action, amount = line.split()
        amount = int(amount)

        if action == 'forward':
            h_pos += amount
            v_pos += aim * amount
        elif action == 'down':
            aim += amount
        elif action == 'up':
            aim -= amount

    print(f'Final positions:\nVertical: {v_pos}\nHorizontal: {h_pos}')
    print(f'Final answer: {h_pos * v_pos}')


if __name__ == "__main__":
    q2()
