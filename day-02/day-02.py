from enum import IntEnum


class ScissorPaperRock(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(IntEnum):
    WIN = 6
    LOSE = 0
    DRAW = 3


def decode_opponent(x):
    return {
            "A": ScissorPaperRock.ROCK,
            "B": ScissorPaperRock.PAPER,
            "C": ScissorPaperRock.SCISSORS
        }[x]


def decode_mine(y):
    return {
            "X": ScissorPaperRock.ROCK,
            "Y": ScissorPaperRock.PAPER,
            "Z": ScissorPaperRock.SCISSORS
        }[y]


def decide_battle(mine, opponent):
    """ Decide who wins """

    if mine == ScissorPaperRock.ROCK and opponent == ScissorPaperRock.SCISSORS or \
       mine == ScissorPaperRock.PAPER and opponent == ScissorPaperRock.ROCK or \
       mine == ScissorPaperRock.SCISSORS and opponent == ScissorPaperRock.PAPER:
        return Result.WIN

    if mine is opponent:
        return Result.DRAW

    return Result.LOSE

def solve_puzzle():
    total_score = 0

    # read file
    with open("day-02-input.txt", "r") as f:
        line = f.readline()
        while line != '':
            input = line.replace("\n", "").split(" ")
            opponent = decode_opponent(input[0])
            my = decode_mine(input[1])

            result = decide_battle(my, opponent)
            score = int(my) + int(result)
            print(f" {my} + {result} = {int(score)}")
            total_score += score

            line = f.readline()

    print(total_score)

if __name__ == "__main__":
    solve_puzzle()