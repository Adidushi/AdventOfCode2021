def q1():
    with open('day 1\input.txt', 'r') as f:
        input = f.readlines()

    counter = 0

    previous_line = int(input[0])

    for line in input[1:]:
        if int(line) > previous_line:
            counter += 1
        previous_line = int(line)
    return counter


def q2():
    with open('day 1\input.txt', 'r') as f:
        input = f.readlines()

    previous_sliding = [int(input[0]), int(input[1]), int(input[2])]

    counter = 0

    for index, line in enumerate(input[1:-2]):
        index += 1

        previous_sum = sum(previous_sliding)

        current_sliding = int(line), int(input[index+1]), int(input[index+2])
        current_sum = sum(current_sliding)

        if current_sum > previous_sum:
            counter += 1
        previous_sliding = current_sliding
    return counter


if __name__ == "__main__":
    print(q1())
    print(q2())
