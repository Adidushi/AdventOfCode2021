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

def remove_unmatched(value, index, lst):
    return [number for number in lst if number[index] == value]

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

def q2():
    with open('day 3\input.txt', 'r') as f:
        input = f.readlines()
    
    list_per_digit = digit_list(input)

    most_common_number = ''.join([most_common(digit) for digit in list_per_digit])
    least_common_number = ''.join([least_common(digit) for digit in list_per_digit])

    oxy, co2 = '', ''

    biggest = [num.strip() for num in deepcopy(input)]
    idx = 0
    # get the first value
    while len(biggest) > 1 and idx < 12:
        dig = most_common(list_per_digit[idx])
        survivors = list()
        for num in biggest:
            if num[idx] == dig:
                survivors.append(num)
        idx += 1
        biggest = survivors
        if len(biggest) == 1:
            print(biggest)
            oxy = biggest[0]

    smallest = [num.strip() for num in deepcopy(input)]
    idx = 0
    # get the first value
    while len(smallest) > 1 and idx < 12:
        survivors = list()
        for num in smallest:
            if num[idx] == least_common_number[idx]:
                survivors.append(num)
        idx += 1
        smallest = survivors
        if len(smallest) == 1:
            print(smallest)
            co2 = smallest[0]

    return oxy, co2


if __name__ == "__main__":
    oxy, co2 = q2()
    print(bin_to_dec(oxy) * bin_to_dec(co2))