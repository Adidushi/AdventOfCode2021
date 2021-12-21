from dataclasses import dataclass
import dataclasses
from functools import lru_cache


class Die:
    def __init__(self):
        self.value = 1
        self.counter = 0

    def roll(self, rolls=1) -> int:
        return_value = 0
        self.counter += rolls
        for _ in range(rolls):
            return_value += self.value
            self.value += 1
            if self.value > 100:
                self.value = 1
        return return_value


@dataclass
class Player:
    score: int
    pos: int
    die: Die

    def __eq__(self, other):
        return self.score == other.score and self.pos == other.pos

    def do_turn(self):
        r = self.die.roll(3)
        new_pos = (self.pos + r)
        while new_pos > 10:
            new_pos -= 10
        self.pos = new_pos
        self.score += self.pos
        return self.score >= 1000


def q1():
    die = Die()
    p1 = Player(0, 10, die)
    p2 = Player(0, 9, die)

    while True:
        if p1.do_turn():
            break
        if p2.do_turn():
            break

    return min(p1.score, p2.score) * die.counter


@dataclass
class Game:
    p1: Player
    p2: Player
    p1_turn: True
    turn: int
    max_score: int

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2 and self.p1_turn == other.p1_turn and self.turn == other.turn and self.max_score == other.max_score

    def __hash__(self):
        return hash(str(self))

    def deep_copy(self):
        new_player1 = Player(self.p1.score, self.p1.pos, self.p1.die)
        new_player2 = Player(self.p2.score, self.p2.pos, self.p2.die)
        return Game(new_player1, new_player2, self.p1_turn, self.turn, self.max_score)

    def advance_player(self, roll):
        if self.p1_turn:
            self.p1.pos += roll
        else:
            self.p2.pos += roll

        if self.turn == 3:
            if self.p1_turn:
                while self.p1.pos > 10:
                    self.p1.pos -= 10
                self.p1.score += self.p1.pos
            else:
                while self.p2.pos > 10:
                    self.p2.pos -= 10
                self.p2.score += self.p2.pos

            self.p1_turn = not self.p1_turn
            self.turn = 0

    def roll(self):
        self.turn += 1
        games = [self.deep_copy() for _ in range(3)]

        for index, game in enumerate(games):
            roll = index + 1
            game.advance_player(roll)

        return games

    def isnt_complete(self):
        return self.p1.score < 21 and self.p2.score < 21

    def is_p1_the_winner(self):
        return self.p1.score >= 21


def q2():
    games = dict()
    player1 = Player(0, 10, None)
    player2 = Player(0, 9, None)

    games[Game(player1, player2, True, 0, 21)] = 1
    while any(map(Game.isnt_complete, games.keys())):
        states = dict()
        for game, count in games.items():
            if not game.isnt_complete():
                if game in states:
                    states[game] += count
                else:
                    states[game] = count
            else:
                more_games = game.roll()
                for more_game in more_games:
                    if more_game in states:
                        states[more_game] += count
                    else:
                        states[more_game] = count

        games = states

    p1_wins, p2_wins = 0, 0
    for game, count in games.items():
        if game.is_p1_the_winner():
            p1_wins += count
        else:
            p2_wins += count

    return max(p1_wins, p2_wins)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
