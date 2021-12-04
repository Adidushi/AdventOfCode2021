class Board:
    def __init__(self, nums):
        self.nums = [line.strip().split() for line in nums]
        self.is_marked = list()
        for _ in range(5):
            line = list()
            for __ in range(5):
                line.append(False)
            self.is_marked.append(line)

    def mark_num(self, num_to_check):
        for i in range(5):
            for j in range(5):
                if self.nums[i][j] == num_to_check:
                    self.is_marked[i][j] = True

    def is_winning(self):
        # Check horizontals
        for line in self.is_marked:
            if all(line):
                return True
        
        # Check verticals
        for line in list(zip(*self.is_marked)):
            if all(line):
                return True
        
        return False

    def calc_remaining(self):
        score = 0
        for i in range(5):
            for j in range(5):
                if not self.is_marked[i][j]:
                    score += int(self.nums[i][j])
        return score
        
def has_numbers(inputString):
     return any(char.isdigit() for char in inputString)

def check_last_board(boards, rolls):
    if len(boards) == 1:
        if boards[0].is_winning():
            return boards[0].calc_remaining() * get_previous_num(rolls[0])
        else:
            boards[0].mark_num(rolls[0])
            return check_last_board(boards, rolls[1:])
    next_boards = list()
    for board in boards:
        board.mark_num(rolls[0])
        if not board.is_winning():
            next_boards.append(board)
    return check_last_board(next_boards, rolls[1:])

def q1():
    with open('day 4\input.txt', 'r') as f:
        input = f.readlines()

    rolls = input[0].strip().split(',')
    input = input[2:]
    
    boards = list()
    curr_board = list()
    for line in input:
        if not has_numbers(line):
            boards.append(Board(curr_board))
            curr_board = list()
        else:
            curr_board.append(line)
    
    for num in rolls:
        for board in boards:
            board.mark_num(num)
            if board.is_winning():
                return board.calc_remaining() * int(num)
    
def q2():
    with open('day 4\input.txt', 'r') as f:
        input = f.readlines()


    rolls = input[0].strip().split(',')
    input = input[2:]
    
    boards = list()
    curr_board = list()
    for line in input:
        if not has_numbers(line):
            boards.append(Board(curr_board))
            curr_board = list()
        else:
            curr_board.append(line)

    return check_last_board(boards, rolls)

def get_previous_num(num):
    with open('day 4\input.txt', 'r') as f:
        input = f.readlines()

    rolls = input[0].strip().split(',')

    index_of_num = rolls.index(num)
    return int(rolls[index_of_num-1])

if __name__ == '__main__':
    print(f'Part 1: {q1()}')
    print(f'Part 2: {q2()}')