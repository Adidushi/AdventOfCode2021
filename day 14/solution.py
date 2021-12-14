from collections import Counter


def parse(input):
    chain = input[0]

    rules = dict()
    for line in input[2:]:
        pre, post = line.split(' -> ')
        rules[pre] = post

    return chain, rules


def apply_step(chain, rules):
    new_chain = ''

    for prev, curr in zip(chain, chain[1:]):
        to_check = prev + curr
        if rules.get(to_check):
            new_chain += prev + rules[to_check]
        else:
            new_chain += prev

    new_chain += chain[-1]

    return new_chain


def add_if_not(d, v, amt=1):
    if v in d:
        d[v] += amt
    else:
        d[v] = amt
    return d


def apply_step2(chain, rules):
    new_chain = dict()
    for pair, occ in chain.items():
        pair1 = pair[0] + rules[pair]
        pair2 = rules[pair] + pair[1]
        for p in (pair1, pair2):
            new_chain = add_if_not(new_chain, p, amt=occ)
    return new_chain


def add_pair(d, pair, amt=1):
    for ch in pair:
        d = add_if_not(d, ch, amt=amt)
    return d


def q1(days):
    with open('day 14\input.txt', 'r') as f:
        input = f.read().splitlines()

    chain, rules = parse(input)

    for _ in range(days):
        chain = apply_step(chain, rules)

    occ = Counter(''.join(chain.split())).most_common()
    most_common = occ[0]
    least_common = occ[-1]
    return most_common[1] - least_common[1]


def q2(days):
    with open('day 14\input.txt', 'r') as f:
        input = f.read().splitlines()

    chain, rules = parse(input)

    first, last = chain[0], chain[-1]

    new_chain = dict()

    for prev, curr in zip(chain, chain[1:]):
        add_if_not(new_chain, prev+curr)

    for _ in range(days):
        new_chain = apply_step2(new_chain, rules)

    char_dict = dict()
    add_pair(char_dict, first)
    add_pair(char_dict, last)
    for k, v in new_chain.items():
        add_pair(char_dict, k, amt=v)

    max_ch = max(char_dict.items(), key=lambda x: x[1])[1]
    min_ch = min(char_dict.items(), key=lambda x: x[1])[1]
    return (max_ch-min_ch)//2


if __name__ == '__main__':
    print(f'Part 1: {q1(10)}')
    print(f'Part 2: {q2(40)}')
