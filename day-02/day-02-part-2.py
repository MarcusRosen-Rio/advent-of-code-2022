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


def decode_outcome(z):
    return {
        "X": Result.LOSE,
        "Y": Result.DRAW,
        "Z": Result.WIN
    }[z]


def decide_hand_based_on_outcome(opponent, outcome):

    if outcome == Result.WIN:

        if opponent == ScissorPaperRock.ROCK:
            return ScissorPaperRock.PAPER
        elif opponent == ScissorPaperRock.PAPER:
            return ScissorPaperRock.SCISSORS
        elif opponent == ScissorPaperRock.SCISSORS:
            return ScissorPaperRock.ROCK

    if outcome == Result.DRAW:
        return opponent

    else:

        if opponent == ScissorPaperRock.ROCK:
            return ScissorPaperRock.SCISSORS
        elif opponent == ScissorPaperRock.PAPER:
            return ScissorPaperRock.ROCK
        elif opponent == ScissorPaperRock.SCISSORS:
            return ScissorPaperRock.PAPER


def solve_puzzle():

    total_score = 0

    # read file
    with open("day-02-input.txt", "r") as f:
        line = f.readline()
        while line != '':
            input = line.replace("\n", "").split(" ")

            # Decode Opponent and outcome
            opponent = decode_opponent(input[0])
            outcome = decode_outcome(input[1])

            # Decide hand based on outcome
            my_hand = decide_hand_based_on_outcome(opponent, outcome)

            # Sum up score
            score = int(my_hand) + int(outcome)
            print(f" {my_hand} + {outcome} = {int(score)}")
            total_score += score

            line = f.readline()

    print(total_score)

if __name__ == "__main__":
    solve_puzzle()