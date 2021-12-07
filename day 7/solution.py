def calc_consumption(distance):
    return distance * (distance + 1) / 2

def q1():
    with open('day 7\input.txt', 'r') as f:
        input = f.read()
    input = [int(num) for num in input.strip().split(',')]

    # avg = round(sum(input) / len(input))

    fuel_consumption = list()

    for pos in range(min(input), max(input)):
        fuel_consumption.append(sum([abs(num - pos) for num in input]))

    return min(fuel_consumption)

    # return sum(fuel_consumption)





    
def q2():
    with open('day 7\input.txt', 'r') as f:
        input = f.read()
    input = [int(num) for num in input.strip().split(',')]

    fuel_consumption = list()

    for pos in range(min(input), max(input)):
        fuel_consumption.append(sum([calc_consumption(abs(num - pos)) for num in input]))

    return min(fuel_consumption)


if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')