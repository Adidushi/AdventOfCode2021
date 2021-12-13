from collections import Counter
from copy import deepcopy


def bin_to_dec(num):
    final_num = 0
    for index, bit in enumerate(num[::-1]):
        final_num += int(bit) * (2 ** index)

    return final_num


def most_common(lst):
    commons = Counter(lst).most_common()

    if commons[0][1] == commons[1][1]:
        return '1'
    return commons[0][0]


def least_common(lst):
    commons = Counter(lst).most_common()

    if commons[1][1] == commons[0][1]:
        return '0'
    return commons[1][0]


def digit_list(lst):
    final_lst = ['', '', '', '', '', '', '', '', '', '', '', '']
    for line in lst:
        line = line.strip()
        for index, ch in enumerate(line):
            final_lst[index] += ch
    return final_lst


def q1():
    with open('day 3\input.txt', 'r') as f:
        input = f.readlines()

    gamma = ''
    epsilon = ''

    list_per_digit = digit_list(input)

    for digit in list_per_digit:
        gamma += most_common(digit)
        epsilon += least_common(digit)

    gamma = bin_to_dec(gamma)
    epsilon = bin_to_dec(epsilon)

    return gamma * epsilon


def filter_options_oxy(lst, index):

    if len(lst) == 1:
        return lst[0]

    digit_list = [num[index] for num in lst]
    digit = most_common(digit_list)

    new_list = list()
    for number in lst:
        if number[index] == digit:
            new_list.append(number)

    return filter_options_oxy(new_list, index+1)


def filter_options_co2(lst, index):

    if len(lst) == 1:
        return lst[0]

    digit_list = [num[index] for num in lst]
    digit = least_common(digit_list)

    new_list = list()
    for number in lst:
        if number[index] == digit:
            new_list.append(number)

    return filter_options_co2(new_list, index+1)


def q2_2():
    with open('day 3\input.txt', 'r') as f:
        input = f.readlines()

    input = [line.strip() for line in input]

    oxy = filter_options_oxy(input, 0)
    co2 = filter_options_co2(input, 0)
    return oxy, co2


if __name__ == "__main__":
    oxy, co2 = q2_2()
    print(bin_to_dec(oxy) * bin_to_dec(co2))
