from typing import Generator, Iterator


def q1():
    with open('day 8\input.txt', 'r') as f:
        input = f.readlines()
    
    entries = [line.strip().split(' | ')[1].split() for line in input]
    
    good_lens = (2, 3, 4, 7)

    total = 0

    for entry in entries:
        for code in entry:
            total += 1 if len(code) in good_lens else 0

    return total

def is_in(num1, num2):
	return all(char in num2 for char in num1)

def sort(s):
	return "".join(sorted(s))

def shared_chars(num1, num2):
    return sum(char in num2 for char in num1)

def derive_map(digits):
	digits = [sort(x) for x in digits]

	d1 = next(x for x in digits if len(x) == 2)
	d4 = next(x for x in digits if len(x) == 4)
	d7 = next(x for x in digits if len(x) == 3)
	d8 = next(x for x in digits if len(x) == 7)
	d9 = next(x for x in digits if len(x) == 6 if is_in(d4, x))
	d3 = next(x for x in digits if len(x) == 5 if is_in(d1, x))
	d0 = next(x for x in digits if len(x) == 6 if x != d9 and shared_chars(d1, x) == 2)
	d6 = next(x for x in digits if len(x) == 6 if x != d9 and x != d0)
	d5 = next(x for x in digits if len(x) == 5 if is_in(x, d6))
	d2 = next(x for x in digits if len(x) == 5 if x != d5 if x != d3)
	Generator
	return {
		d0: "0",
		d1: "1",
		d2: "2",
		d3: "3",
		d4: "4",
		d5: "5",
		d6: "6",
		d7: "7",
		d8: "8",
		d9: "9",
	}

def parse(s):
	a, b = s.split(" | ")
	return a.split(" "), b.split(" ")

def q2():
    with open('day 8\input.txt', 'r') as f:
        input = f.read()
    data = list(map(parse, input.split('\n')))

    out = 0

    for x, y in data:
        out += int("".join(derive_map(x)[sort(d)] for d in y))

    return out

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')