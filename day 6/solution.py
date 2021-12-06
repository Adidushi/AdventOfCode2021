from dataclasses import dataclass


@dataclass
class Fish:
    days: int

    def next_day(self):
        if self.days == 0:
            self.days = 6
            return Fish(8)
        self.days -= 1


def do_day(index, fish_list):
    if index == 0:
        return len(fish_list)

    new_fish_list = list()
    for fish in fish_list:
        new_fish = fish.next_day()
        if new_fish:
            new_fish_list.append(new_fish)

    fish_list.extend(new_fish_list)

    return do_day(index-1, fish_list)


def q1(max_days):
    with open('day 6\input.txt', 'r') as f:
        input = f.readlines()

    input = [int(num)
             for num in input[0].strip().split(',')]  # list of numbers

    fish_list = [Fish(days) for days in input]

    return do_day(max_days, fish_list)


def better_algorithm(max_days):
    with open('day 6\input.txt', 'r') as f:
        input = f.readlines()

    input = [int(num)
             for num in input[0].strip().split(',')]  # list of numbers

    counter = [0] * 9
    for fish in input:
        counter[fish] += 1
    births = 0

    for day in range(max_days):
        # print(f'Current day: {day}, current pop: {sum(counter)}')
        births = counter.pop(0)
        counter[6] += births
        counter.append(births)

    return sum(counter)


if __name__ == '__main__':
    days_p1 = 80
    days_p2 = 256

    print(f'Part 1: {better_algorithm(days_p1)}')
    print(f'Part 2: {better_algorithm(days_p2)}')
