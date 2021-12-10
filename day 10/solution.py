def find_score(opening, closing, score, line):
    stack = list()

    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            ix = closing.index(char)
            if opening.index(stack[-1]) == ix:
                stack = stack[:-1]
            else:
                return score[ix]
    return 0


def q1():
    with open('day 10\input.txt', 'r') as f:
        input = f.read().splitlines()
    opening = list('([{<')
    closing = list(')]}>')
    score = [3, 57, 1197, 25137]

    total = 0
    for line in input:
        total += find_score(opening, closing, score, line)

    return total


def find_remaining(opening, closing, score, line):
    stack = list()

    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            stack = stack[:-1]

    ret_value = 0

    for char in reversed(stack):
        ret_value *= 5
        char_ix = opening.index(char)
        ret_value += score[char_ix]

    return ret_value


def q2():
    with open('day 10\input.txt', 'r') as f:
        input = f.read().splitlines()

    opening = list('([{<')
    closing = list(')]}>')
    score = [3, 57, 1197, 25137]
    filtered_input = [line for line in input if not find_score(
        opening, closing, score, line)]
    new_score = [1, 2, 3, 4]

    scores = sorted([find_remaining(opening, closing, new_score, line)
                    for line in filtered_input])
    return scores[(len(scores)-1)//2]


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')
